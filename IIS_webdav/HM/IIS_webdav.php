<?php  //添加数据
include("conn.php");
$psotip=$_SERVER["REMOTE_ADDR"];   #获取提交服务器的IP
$tim=date('Y-m-d H:i:s',time());
//http://xxxx.com/IIS_webdav.php?URL=aaaaa
$sql="insert into IIS_webdav (url,postIP,time) VALUES ('$_REQUEST[URL]','$psotip','$tim')";
//print $sql;
mysql_query($sql)or die("添加数据错误!!!11122222222");
print "添加数据成功！！222";
?>


