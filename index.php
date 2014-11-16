<?php
	function mostrar($string)
	{
		echo "<p>";
		echo $string;
		echo "</p>";
	}

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

	function mostrar_datos($objeto)
	{
		mostrar($objeto->{'idMovie'});
		mostrar($objeto->{'nameMovie'});
		mostrar($objeto->{'descriptionMovie'});
		mostrar($objeto->{'yearMovie'});
		echo "<br>";
	}

	function send_data($url, $data)
	{
		$ch = curl_init($url);
		curl_setopt($ch, CURLOPT_POST, 1);
		curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
		curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
		curl_setopt($ch, CURLOPT_HEADER, 0);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);

		$response = curl_exec($ch);
		return $response;
	}

	include ("index.html");

 ?>