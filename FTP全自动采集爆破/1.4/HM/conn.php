<?php
//=================================
$conn = @mysql_connect('localhost:3306','root','316118740') or die("连接数据库错误!!!");  //连接数据库
mysql_select_db('hhmm',$conn) or die("打开数据错误!!!");  //打开数据
mysql_query("set names 'GBK'"); //使用GBK中文编码;

//=================================
?>
