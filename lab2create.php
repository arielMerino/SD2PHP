<?php  
	function alert($msg)
	{
		echo '<script type="text/javascript">';
		echo 'alert ("';
		echo $msg;
		echo '")';
		echo '</script>' ;
	}
	include("lab2create.html");
?>