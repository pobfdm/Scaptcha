# Scaptcha

run make_base.py for creating captcha.

How to use it:
```
<?php 
include ('base.php');
$rand_captcha = array_rand($captcha, 1);


if (isset($_POST["send"]))
{
	$myval=$_POST["myval"];
	$captchaid=$_POST["captchaid"];
	if ($myval==$captcha[$captchaid])
	{
		echo '<h2>Captcha OK</h2>';
	}else{
		echo '<h2>Captcha not correct</h2>';
		}

}
 
?>

<!DOCTYPE html>
<html>
	<head>
	<title>test captcha</title>
	</head>
	<body>
		<h1>Test captcha</h1>
		<p>A form width captcha</p>
		<form method="POST" action="index.php">
			<input type="hidden"  name="captchaid" value="<?php echo $rand_captcha ?>">
			<img src="image.php?id=<?php echo $rand_captcha ?>" />
			<input type="text" value="" name="myval">
			<button type="submit" name="send">send</button>
			</form>
		</body>
	</html>

```
