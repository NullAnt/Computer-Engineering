import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
public class SimpleJDBCExample {
 // JDBC URL, username, and password of MySQL server
 private static final String URL = "jdbc:mysql://localhost:3306/testdb"; // Ensure your database 'testdb' exists
 private static final String USER = "root";
 private static final String PASSWORD = "password";
 public static void main(String[] args) {
 Connection connection = null;
 Statement statement = null;
 ResultSet resultSet = null;
 try {
 // Load and register JDBC driver for MySQL
 Class.forName("com.mysql.cj.jdbc.Driver");
 // Establish the connection
 connection = DriverManager.getConnection(URL, USER, PASSWORD);
 System.out.println("Connection established successfully!");
 // Create a statement
 statement = connection.createStatement();
 // Create a table if it doesn't exist
 String createTableSQL = "CREATE TABLE IF NOT EXISTS users (" +
 "id INT AUTO_INCREMENT PRIMARY KEY, " +
 "name VARCHAR(50) NOT NULL, " +
 "email VARCHAR(50) NOT NULL)";
 statement.executeUpdate(createTableSQL);
 System.out.println("Table 'users' created successfully!");
 // Insert a record
 String insertQuery = "INSERT INTO users (name, email) VALUES ('John Doe',
'john@example.com')";
 statement.executeUpdate(insertQuery);
 System.out.println("Record inserted successfully!");
 // Execute a query to retrieve data
 String selectQuery = "SELECT * FROM users";
 resultSet = statement.executeQuery(selectQuery);
 // Process the result set
 while (resultSet.next()) {
 int id = resultSet.getInt("id");
 String name = resultSet.getString("name");
 String email = resultSet.getString("email");
 System.out.println("ID: " + id + ", Name: " + name + ", Email: " + email);
 }
 } catch (ClassNotFoundException e) {
 System.out.println("MySQL JDBC Driver not found.");
 e.printStackTrace();
 } catch (SQLException e) {
 e.printStackTrace();
 } finally {
 // Close the result set, statement, and connection
 try {
 if (resultSet != null) resultSet.close();
 if (statement != null) statement.close();
 if (connection != null) connection.close();
 System.out.println("Connection closed successfully!");
 } catch (SQLException e) {
 e.printStackTrace();
 }
 }
 }
}