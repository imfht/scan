<?php
//=================================
$conn = @mysql_connect('localhost','hacksa3124','2FA424E200164e') or die("连接数据库错误!!!");  //连接数据库
mysql_select_db('hacksa3124',$conn) or die("打开数据错误!!!");  //打开数据
mysql_query("set names 'GBK'"); //使用GBK中文编码;

//=================================
?>
