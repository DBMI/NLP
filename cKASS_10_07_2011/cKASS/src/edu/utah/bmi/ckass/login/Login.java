package edu.utah.bmi.ckass.login;

import java.io.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

import javax.servlet.*;
import javax.servlet.http.*;

public class Login extends HttpServlet {
	private static final long serialVersionUID = 1L;
	public void doGet(HttpServletRequest req, HttpServletResponse resp)
		throws ServletException, IOException {	
		resp.setContentType("text/html;charset=ISO-8859-1");
		//resp.setContentType("text/html");
		PrintWriter out = resp.getWriter();
		Connection con = null;
		Statement stmt = null;
		ResultSet rs = null;
		String sql = null;
		String husername = (String) req.getParameter("username");
		String hpassword = (String) req.getParameter("password");

		int i = 0; 
		String tusername =""; 
		String tpassword =""; 
		Integer tuid = null ;  

		try {
			Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");
			
		  } catch(java.lang.ClassNotFoundException e) {
		        System.err.println("class.forName: "+ e.getMessage());
		    }
		
		try {
			con = DriverManager.getConnection("jdbc:mysql://localhost:3306/","root","123456");
			
			//out.println("<P>Connect Successful!!");
			stmt = con.createStatement();
			//out.println("<P>CreateStatement Successful!");			
			sql = "select * from ckass.user where username='" + husername + "'";
			
			out.println(sql);
			//sql = "select * from user where username = husername" ;
			//out.println(sql);
			//sql = "select * from user where username = husername" ;
			rs = stmt.executeQuery(sql);
			
			//out.println("<P>ResultSet rs Successful!");
		}
		catch (Exception e) {    
				e.printStackTrace();	
		}

	  	try {
	  		while (rs.next()) {
	  			//out.println("<P>Select Successful!");
	  			i++;
	  			//out.println("<P>i="+i);
	  			tusername = rs.getString("username");
	  			tpassword = rs.getString("password");
	  			tuid = rs.getInt("uid");
	  			
  				if (tpassword.trim().equals(hpassword.trim())) {
	  				  					
  					HttpSession session = req.getSession(true);
		  			session.setAttribute("username",tusername);
		  			session.setAttribute("uid",tuid);
		  			
		  			
		  				resp.sendRedirect("../pages/MainFrame.jsp"); }
					else {
  					
  					   resp.sendRedirect("../pages/Login.html");	
	  			}
	  		}
	  		
		}	
	  	catch (Exception e) {  
    		e.printStackTrace();	
    	}
 
	  	try {
	  		rs.close();
	  		stmt.close();
	  		con.close();
	  	}
	  	catch (Exception e) { 
    		e.printStackTrace();
        }
	}
}
