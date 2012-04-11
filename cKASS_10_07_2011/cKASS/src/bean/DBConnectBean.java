package bean;
import java.sql.*;

public class DBConnectBean {
    
    String DBDriver="com.mysql.jdbc.Driver";
    String ConnStr="jdbc:mysql://localhost:3306/";
    Connection conn=null;
    Statement stmt = null;
    ResultSet RS=null;
    int i=0;
	
    public DBConnectBean() {
        try {
	        
	        Class.forName(DBDriver);
	    } catch(java.lang.ClassNotFoundException e) {
	        System.err.println("class.forName: "+e.getMessage());
	    }
    }
    
    public ResultSet executeQuery(String sql) {
	//Data Query
    	//System.out.println("DBConnectBean: "+sql);
        try {
           //connect to DB
 	       conn = DriverManager.getConnection(ConnStr,"root","root");
 	       Statement stmt = conn.createStatement();
           RS = stmt.executeQuery(sql);
        }
        catch(SQLException ex) {
          System.err.println("aq.executeQuery:"+ex.getMessage());
        }
        return RS;
    }  // end of executeQuery
    
    public int executeUpdate(String sql) {
	//update, delete, insert data
    	//System.out.println("DBConnectBean: "+sql);
        i = 0;
        try {
           //connect to DB
           conn = DriverManager.getConnection(ConnStr);
           Statement stmt = conn.createStatement();
           i = stmt.executeUpdate(sql);
        }
        catch(SQLException ex) {
          System.err.println("aq.executeQuery:"+ex.getMessage());
        }
        return i;
    }  // end of executeUpdate
}  // end of class DBConnectBean
