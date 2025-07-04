<?php

if (isset($_POST['su'])) {
    $distunce = 579;
    $planet = "mercury";
} else if (isset($_POST['ji'])) {
    $distunce = 1500;
    $planet = "earth";
} else if (isset($_POST['wha'])) {
    $distunce = 2300;
    $planet = "mars";
} 

if (@$distunce) {
    $speedOfLight = 3;
    $min = round($distunce / $speedOfLight * (1/60), 2);
    echo "Travle time from Sun to {$planet} : {$min} minutes";
} else {
    echo "Wrong access";
}

?>