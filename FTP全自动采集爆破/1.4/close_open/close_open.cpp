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

int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
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
				ShellExecute( 0,"open",argv[2],NULL,NULL,SW_SHOWMAXIMIZED);
		}
		else
			//MessageBox(NULL,"text","结束进程失败！",MB_OK);
			printf ("结束进程失败！\n");
	}
}


