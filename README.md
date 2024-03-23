# DATA225-Lab1
   
1. Connect to MySQL. 
   Run :
   drop database tmdb;
   create database tmdb;
   use tmdb;
   
2. Run dd.sql to create tables

3. Download the ZIP and unzip in the desired path

4. Configure MySQL url, username and password in configuration.properties
   Ex :
   mysql.url=jdbc:mysql://localhost:3306/tmdb
   mysql.user=abcd
   mysql.pass=abcd
   
5. Run from inside the TMDB directory
   java -cp dependencies/json.jar:dependencies/mysql-connector-java.jar:tmdb.jar Populate
