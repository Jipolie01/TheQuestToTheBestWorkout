<?php
session_start();
/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

    //do this when username password combination is correct
    $email = $_POST['email'];
    
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
    
    else {
        //print("Connected successfully\n"); 
        $sql = ("SELECT * FROM testtable");//Where username='$email'
        $result = $conn->query($sql);
        
        if (!empty($result)){
            foreach ($result as $row){
                
                if ($row['username'] == $email && $row['password'] == $_POST['password']){
                    $_SESSION['username'] = $email;
                    $_SESSION['goneBack'] = FALSE;
                    //goto next page
                    header("Location: ./loggedIn.php");
                    
                }
                else{
                    $_SESSION['goneBack'] = TRUE;
                    //go back
                    header("Location: ./index.php");
                }
            }
        }
        else{
            $_SESSION['goneBack'] = TRUE;
            //go back
            header("Location: ./index.php");
        }
    }
    $conn->close();
?>