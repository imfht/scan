<?php
//=================================
$conn = @mysql_connect('58.64.189.96:3306','ryyt225','kx9YK14hzI') or die("连接数据库错误!!!");  //连接数据库
mysql_select_db('ryyt225',$conn) or die("打开数据错误!!!");  //打开数据
mysql_query("set names 'GBK'"); //使用GBK中文编码;

//=================================
?>
