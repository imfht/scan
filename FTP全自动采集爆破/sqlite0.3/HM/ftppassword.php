<?php  //添加数据
include("conn.php");
//$_REQUEST["IP"]; //玉米
//$_REQUEST["user"]; //用户名
//$_REQUEST["password"]; //密码
$ftproot=$_REQUEST["root"]; //权限
$psotip=$_SERVER["REMOTE_ADDR"];   #获取提交服务器的IP
$tim=date('Y-m-d H:i:s',time());
//http://xxxx.com/ftppassword.php?IP=www.baidu.com&user=1111&password=2222&root=2

if ($ftproot==2)
{
$sql="insert into ftppassword2(IP,user,password,root,postIP,html,time) VALUES('$_REQUEST[IP]','$_REQUEST[user]','$_REQUEST[password]','2','$psotip','html','$tim')";
//print $sql;
mysql_query($sql)or die("添加数据错误!!!11122222222");
print "添加数据成功！！222";
}

if ($ftproot==3)
{
$sql="insert into ftppassword3(IP,user,password,root,postIP,html,time) VALUES('$_REQUEST[IP]','$_REQUEST[user]','$_REQUEST[password]','3','$psotip','html','$tim')";
//print $sql;
mysql_query($sql)or die("添加数据错误!!!33333333");
print "添加数据成功！！333";
}
//print $sql;
?>


