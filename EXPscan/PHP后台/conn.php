<?php
//=================================
$conn = @mysql_connect('localhost:3306', 'root', '316118740') or die("连接数据库错误!!!");  //连接数据库
mysql_select_db('999kankan',$conn) or die("打开数据错误!!!");  //打开数据
//mysql_query("SET NAMES UTF8");
//mysql_query("set character_set_client=utf8"); 
//mysql_query("set character_set_results=utf8");
mysql_query("set names 'GBK'"); //使用GBK中文编码;

//=================================
?>
