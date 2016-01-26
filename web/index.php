<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<?php
    session_start();
    if (isset($_SESSION['username'])){
        unset($_SESSION['username']);
    }
?>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="style.css">
        <title>
            
        </title>
    </head>
    <body>
        
        
        <image src="Images/strongman.png" width="150" height="150" style="position: fixed; left: 25%;"><image src="Images/logo.png" width="487.5" height="150" style="position: fixed; left: 40%;"/>
        <div class="navigationBar">
            <h4>Menu</h4>
            <button target="pages" class="navigationButton">Change user information</button><br>
        </div>
        
        <div class="mainpage" id="pages">
            <?php
                if (isset($_SESSION['goneBack']) and $_SESSION['goneBack'] == TRUE){
                    print('<center><h3>The email or password was incorrect. Please try again</h3></center>');
                }
            ?>
            <div class="logindiv">
                <form action="login.php" method="post">
                    <h3>Please insert your login information</h3><br>
                    <div style="width: 350px;">
                        E-mail:&nbsp &nbsp &nbsp<input type="text" name="email" style="right: 10px;">
                    </div><br>
                
                    <div style="width: 350px;">
                        Password: <input type="password" name="password" style="right: 10px;">
                    </div>
                    <input type="submit" class="navigationButton" value="Submit">
                </form>
            </div>
        </div>
        
    </body>
</html>
<!--
target frames met buttons
en om de informatie uit de database te editen moet je value= gebruiken wat zorgt dat het de oude waarde in de textboxes komt
-->