import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;
public class CreateDatabaseExample {
    // JDBC URL, username, and password of MySQL server
    private static final String URL = "jdbc:mysql://localhost:3306/";
    private static final String USER = "root";
    private static final String PASSWORD = "myBoyGBA!87@";
    // JDBC variables for opening and managing connection
    private static Connection connection;
    private static Statement statement;
    public static void main(String[] args) {
        try {
            // Load and register JDBC driver for MySQL
            Class.forName("com.mysql.cj.jdbc.Driver");
            // Establish the connection
            connection = DriverManager.getConnection(URL, USER, PASSWORD);
            System.out.println("Connection established successfully!");
            // Create a statement
            statement = connection.createStatement();
            // Create a new database
            String createDatabaseSQL = "CREATE DATABASE IF NOT EXISTS testdb";
            statement.executeUpdate(createDatabaseSQL);
            System.out.println("Database 'testdb' created successfully!");
        } catch (ClassNotFoundException e) {
            System.out.println("MySQL JDBC Driver not found.");
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // Close the statement and connection
            try {
                if (statement != null) statement.close();
                if (connection != null) connection.close();
                System.out.println("Connection closed successfully!");
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}