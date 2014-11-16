<?php 
	function get_data($url)
	{
		$ch = curl_init();
		$timeout = 5;
		curl_setopt($ch, CURLOPT_URL, $url);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER,1);
		curl_setopt($ch, CURLOPT_CONNECTTIMEOUT,$timeout);
		$data = curl_exec($ch);
		curl_close($ch);
		return $data;
	}

	function mostrar($string)
	{
		echo "<p>";
		echo $string;
		echo "</p>";
	}

	function alert($msg)
	{
		echo '<script type="text/javascript">';
		echo 'alert ("Se ha actualizado: ';
		echo $msg;
		echo '")';
		echo '</script>' ;
	}
	include ("lab2update.html");
?>