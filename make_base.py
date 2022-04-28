#!/usr/bin/env python3

basefile="base.php"
imagefile="image.php"
ncaptcha=1000;
lencaptcha=5;

import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

script='''

$captchaIndex=$_GET['id'];
$txt=  $captcha[$captchaIndex];

function noise($image)
{
	$x = 100;
	$y = 50;
	$image = imagecreatetruecolor($x,$y);
	$white = imagecolorallocate($image, 255, 255, 255);
	imagefilledrectangle($image, 0, 0, 399, 29, $white);
	$colorText = imageColorAllocate($image, 255,255,255);
	
	for($i = 0; $i < $x; $i++) {
	    for($j = 0; $j < $y; $j++) {
	        $color = imagecolorallocate($image, rand(0,20), rand(0,255), rand(0,255));
	        imagesetpixel($image, $i, $j, $color);
	        
	    }
	}
	return $image;
}

  
$im = imagecreatetruecolor(120, 50);
$im=noise($im);


imagettftext($im, 20, 0, 10, 35, 
            imagecolorallocate($im, 0, 0, 0), 
            './font.ttf', $txt);
  
// Output to browser
header('Content-Type: image/png');
imagepng($im);
imagedestroy($im);
'''

fi = open(imagefile, "w")
fb = open(basefile, "w")

fi.write("<?php \n")
fb.write("<?php \n")



for i in range(ncaptcha):
	index=randomword(10)
	value=randomword(lencaptcha)
	fi.write("$captcha['"+index+"'] = '"+value+"'; ")
	fi.write('\n')
	fb.write("$captcha['"+index+"'] = '"+value+"'; ")
	fb.write('\n')

fi.write(script+'\n')
fi.write("?> ")
fi.close()

fb.write("?> ")
fb.close()

