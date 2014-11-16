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

	function mostrar_datos($objeto)
	{
		mostrar($objeto->{'idMovie'});
		mostrar($objeto->{'nameMovie'});
		mostrar($objeto->{'descriptionMovie'});
		mostrar($objeto->{'yearMovie'});
		echo "<br>";
	}

	include ("lab2read.html");
?>