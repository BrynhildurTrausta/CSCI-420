<html>
<head>

	<title>My index file!</title>

</head>

<body>

<h1>This is amazing!</h1>

<form method="GET">
  <label>Width:</label><input type="text" name="width">
  <label>Height:</label><input type="text" name="height">
  <input type="submit"  value="Make Table!"/>
</form>


<?php
	echo "Hello World!\n";
	echo "<h2>Wow</h2>\n";
	$width = 3;
	$height = 4;
	if(isset($_GET['width']) && isset($_GET['height'])){
	  $width = $_GET['width'];
	  $height = $_GET['height'];
	}

	echo "<table border='1'>\n";
	for ($y = 0; $y < $height; $y++){
	  echo "<tr>\n";
	  for($x = 0; $x < $width; $x++){
	    echo "   <td>";
	    echo $x * $y;
	    echo "</td>\n";
	  }
	  echo "</tr>\n";
	}

	echo "</table>\n";

?>

<table border="1">
<tr>
	<td>One</td>
	<td>Two</td>
</tr>
<tr>
	<td>Three</td>
	<td>Four</td>
</tr>
</table>


</body>

</html>
