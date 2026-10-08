<?php

$database =new PDO("sqlite:users.db");

$database->setAttribute(
	PDO::ATTR_ERRMODE,
	PDO::ERRMODE_EXCEPTION
);

$database->exec("
	CREATE TABLE IF NOT EXISTS users(
		id INTEGER PRIMARY KEY,
		username TEXT UNIQUE
	)
");

$insert = $database->prepare(
	"INSERT OR IGNORE INTO users (username) VALUES (?)"
);

$insert->execute(["diego"]);
$insert->execute(["ale"]);
$insert->execute(["luis"]);

$username = trim($_POST["username"] ?? "");

if ($username == "") {
	echo "Please enter a username.";
	exit;
}

$query =$database->prepare(
	"SELECT username FROM users WHERE username = ?"
);

$query->execute([$username]);

$user = $query->fetch();

if ($user) {
	echo "User found.";
} else {
	echo "User not found.";
}

?>
