<?php
session_start();
if (isset($_SESSION['username'])){
    header("Location: index.php");
}
$username = $_SESSION['username'];
$firstName = $_POST['firstName'];
$lastName = $_POST['lastName'];
$street = $_POST['street'];
$zipCode = $_POST['zipCode'];
$phoneNumber = $_POST['phoneNumber'];
$email = $_POST['email'];
$password = $_POST['password'];

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
    $sql = ("UPDATE testtable SET column1=value, column2=value2 WHERE email = $username");//change to watever the table is with user information
    $result = $conn->execute($sql); 
}
    $conn->close();
?>