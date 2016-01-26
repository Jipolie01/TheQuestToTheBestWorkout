<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<?php
session_start();
?>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" type="text/css" href="style.css">
        <title>
            
        </title>
    </head>
    <body>
        
        <?php 
            if (!isset($_SESSION['username'])){
                header("Location: index.php");
            }
            else{
                $username = $_SESSION['username'];
                //sql get username +user information
                $servername = "localhost";
                $username = "";
                $password = "";
                $db = "test";
                    
                // Create connection
                $conn = new mysqli($servername, $username, $password, $db);
                    
                // Check connection
                if ($conn->connect_error) {
                    die("Connection failed: " . $conn->connect_error);
                }
                
                else{
                    $sql = ("SELECT * FROM testtable WHERE username='$username'");//change to watever the table is with user information
                    $result = $conn->query($sql); 
                    
                    if(!empty($result)){
                        foreach ($result as $row){//Lots of changes needed to be done
                            $firstName = $row['firstName'];
                            $lastName = $row['surname'];
                            $street = $row['street'];
                            $zipCode = $row['zipCode'];
                            $phoneNumber = $row['phoneNumber'];
                            //email = username so no need to grab that again
                            $password = $row['password'];
                            $gender = $row['gender'];
                        }
                    }
                }
                $conn->close();
            } 
        ?>
        <image src="Images/strongman.png" width="150" height="150" style="position: fixed; left: 25%;"><image src="Images/logo.png" width="487.5" height="150" style="position: fixed; left: 40%;"/>
        <div class="navigationBar">
            <h4>Menu</h4>
            <button target="pages" class="navigationButton">Change user information</button><br>
        </div>
        
        <div class="mainpage" id="pages">
            <form action="login.php" method="post">
                <div class="text">
                    <br>
                    First name:<br><br>
                    Last name:<br><br>
                    Street:<br><br>
                    Zipcode:<br><br>
                    Phone number:<br><br>
                    E-mail:<br><br>
                    Password:<br><br>
                    gender:
                </div>
                <div class="textboxesdiv">
                    <input type="text" name="firstName" value="<?php $firstName ?>" class="changeInformation" style="margin-top: 17px;"><br>
                    <input type="text" name="lastName" value="<?php $lastName ?>" class="changeInformation"><br>
                    <input type="text" name="street" value="<?php $street ?>" class="changeInformation"><br>
                    <input type="text" name="zipCode" value="<?php $zipCode ?>" class="changeInformation"><br>
                    <input type="text" name="phoneNumber" value="<?php $phoneNumber ?>" class="changeInformation"><br>
                    <input type="text" name="email" value="<?php $username ?>" class="changeInformation"><br>
                    <input type="password" name="password" value="<?php $password ?>" class="changeInformation"><br>
                    <?php
                    if ($gender == "Male"){
                        print('<input type="radio" name="gender" value=" Male" checked> Male<br>');
                        print('<input type="radio" name="gender" value="Female"> Female<br>');
                    }
                    elseif ($gender == "Female"){
                        print('<input type="radio" name="gender" value=" Male"> Male<br>');
                        print('<input type="radio" name="gender" value="Female" checked> Female<br>');
                    }
                    else{
                        print('<input type="radio" name="gender" value=" Male"> Male<br>');
                        print('<input type="radio" name="gender" value="Female"> Female<br>');
                    }
                    ?>
                </div>
                    <input type="submit" class="navigationButton" value="Submit" style="left: 40%; top: 70%; position: absolute;">
            </form>
        </div>
        
    </body>
</html>
<!--
target frames met buttons
en om de informatie uit de database te editen moet je value= gebruiken wat zorgt dat het de oude waarde in de textboxes komt
-->