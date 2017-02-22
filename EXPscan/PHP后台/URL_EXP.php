<?php  //添加数据
include("conn.php");
$tim=date('Y-m-d H:i:s',time());
//http://xxxx.com/ftppassword.php?IP=www.baidu.com&user=1111&password=2222&root=2
//http://www.999kankan.com/URL_EXP.php?yijuhua=1&url=hao123.com&exp=exp&expR=expaaaa&webshell=http://wwwww.baidu.com&password=1123&bz=4444
//---yijuhua=url=exp=expR=webshell=password=bz=
//["一句话 是否成功0否 1是","网址","严重程度","漏洞类型","漏洞地址","密码","备注"]7个

$sql="insert into exp_sql(yijuhua,url,exp,expR,webshell,password,bz,time) VALUES('$_REQUEST[yijuhua]','$_REQUEST[url]','$_REQUEST[exp]','$_REQUEST[expR]','$_REQUEST[webshell]','$_REQUEST[password]','$_REQUEST[bz]','$tim')";
//print $sql;
mysql_query($sql)or die("添加数据错误!!!33333333");
print "添加数据成功！！333";
//print $sql;
?>


