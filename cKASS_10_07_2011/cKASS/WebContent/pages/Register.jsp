<%@ page import="java.sql.*,java.util.*" language="java"
	contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>iDASH</title>
<link href="../style/style.css" type="text/css" rel="stylesheet" />
</head>
<body>
<center>
<table width="780" cellspacing="0" cellpadding="0" align="center" bgcolor="#f9f9f9">
	<tr>
		<td height="135" valign="top" >
		<table width="100%" height="250"  cellpadding="0" cellspacing="0">
			<tr height="135">
				<td><img src="../images/header_ban.png"></td>
			</tr>
			<tr height="50">
				<td>&nbsp;</td>
			</tr>
			<tr>
				<td align="center" width="185" >
					<form action="" method="get">
						<table>
							<caption>Register</caption>
							<tr>&nbsp;</tr>
							<tr>
								<td> First Name: </td>
								<td> <input type="text" name="firstName" size="20" maxlength="20" align="left"></td>
							</tr>
							<tr height="5">
								<td>&nbsp;</td>
								<td>&nbsp;</td>
							</tr>
							<tr>
								<td >Last Name: </td>
								<td><input type="text" name="lastName" size="20" maxlength="20" align="left"></td>
							</tr>
							<tr height="5">
								<td>&nbsp;</td>
								<td>&nbsp;</td>
							</tr>
							<tr>
								<td >E-Mail: </td>
								<td><input type="text" name="email" size="20" maxlength="20" align="left"></td>
							</tr>
							<tr height="5">
								<td>&nbsp;</td>
								<td>&nbsp;</td>
							</tr>
							<tr>
								<td >User Name: </td>
								<td><input type="text" name="userName" size="20" maxlength="20" align="left"></td>
							</tr>
							<tr height="5">
								<td>&nbsp;</td>
								<td>&nbsp;</td>
							</tr>
							<tr>
								<td >Password: </td>
								<td><input type="password" name="password" size="20" maxlength="20" align="left"></td>
							</tr>
							<tr>
								<td>&nbsp;</td>
								<td>&nbsp;</td>
							</tr>
							<tr>
								<td >Confirm Password: </td>
								<td><input type="password" name="password2" size="20" maxlength="20" align="left"></td>
							</tr>
							<tr>
								<td>&nbsp;</td>
								<td>&nbsp;</td>
							</tr>
							<tr>
								<td align="right">  </td>
								<td align="right"> <input type="submit"  value="Create account"></tr>
						</table>
					</form>
					
					  <jsp:useBean id="DBConnectBean" scope="session" class="edu.utah.bmi.ckass.bean.DBConnectBean" >
  					</jsp:useBean>
<%
	String name ="";
	String value="";  
	
	Enumeration <String> e = request.getParameterNames();

	while (e.hasMoreElements()) {
    	name = e.nextElement();
        value = request.getParameter(name);
        if ( (value==null) || (value.isEmpty())){
        	response.sendRedirect("Register.jsp");
        }
        session.setAttribute(name, value);
    }
    
	
    String firstName = request.getParameter("firstName");
    String lastName = request.getParameter("lastName");
    String email = request.getParameter("email");
    String userName = request.getParameter("userName");
    String password = request.getParameter("password");

    if ( (firstName==null) ||(lastName==null)||(email==null)||(userName==null)||(password==null) ){
    	
    }else {
    	String sql="insert into ckass.user (firstName, lastName, email, userName, password) VALUES ('" 
    		   	+ firstName + "', '" + lastName + "', '" + email + "', '" + userName + "', '" + password + "')";
    			int i=DBConnectBean.executeUpdate(sql);
    			response.sendRedirect("login.html");	
    }
   	 
%>

				</td>
				<td width="430">&nbsp;</td>
                <td width="200" >
	        </tr>
	        <tr height="20">
				<td>&nbsp;</td>
			</tr>
		</table>
		</td>
	</tr>
</table>
</center>
</body>
</html>