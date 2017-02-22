// internet_close.cpp : Defines the entry point for the DLL application.
//检测在线连接状态   http://hi.baidu.com/alalmn

#include "stdafx.h"
#include <Wininet.h>
#pragma comment(lib, "Wininet.lib") 

// extern "C" _declspec(dllexport) int addnum(int num1,int num2);
// int addnum(int num1,int num2)
// {
// return num1+num2;
// }

extern "C" _declspec(dllexport) int Fun_Internet();
int Fun_Internet()
{
  
//#define INTERNET_CONNECTION_MODEM           1
//#define INTERNET_CONNECTION_LAN             2
//#define INTERNET_CONNECTION_PROXY           4
//#define INTERNET_CONNECTION_MODEM_BUSY      8
  
DWORD   flags;//上网方式 
BOOL   m_bOnline=TRUE;//是否在线  

m_bOnline=InternetGetConnectedState(&flags,0);   
if(m_bOnline)//在线   
{   
   if ((flags & INTERNET_CONNECTION_MODEM) ==INTERNET_CONNECTION_MODEM)
   {
//cout<<"在线：拨号上网\n";
	return 1;
   }
   if ((flags & INTERNET_CONNECTION_LAN) ==INTERNET_CONNECTION_LAN)
   {
    //cout<<"在线：通过局域网\n";
	return 2;
   }
   if ((flags & INTERNET_CONNECTION_PROXY) ==INTERNET_CONNECTION_PROXY)
   {
    //cout<<"在线：代理\n";
	return 3;
   }
   if ((flags & INTERNET_CONNECTION_MODEM_BUSY) ==INTERNET_CONNECTION_MODEM_BUSY)
   {
    //cout<<"MODEM被其他非INTERNET连接占用\n";
	return 4;
   }
   return 5;
}
else
{
   //cout<<"不在线\n";
   return 0;
}

}