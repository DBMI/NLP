<%@ page import="java.sql.*"  import="java.sql.*,java.util.*" language="java"
	contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%
	String username = (String) session.getAttribute("username");
	Integer uid = (Integer) session.getAttribute("uid");
%>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Add A New Task</title>
<link href="../style/style.css" type="text/css" rel="stylesheet" />
</head>
<body>
	<center>
		<table>
			<tr>
				<td>
					<table>
						<tr>
							<td width='0px'></td>
							<td><img src="../images/header_ban.png" ></td>
						</tr>
					</table></td>
			</tr>
			<tr>
				<td align="left">
					<table>
						<tr>
							<td>
								<div id="navigation">
									<ul>
										<li><a href="MyWorkspace.jsp">My WorkSpace</a>
										</li>
										<li><a href="CreateKB.jsp">Create Knowledge Base</a>
										</li>
										<li><a href="Search.jsp">Search</a>
										</li>
										<li><a href="Browse.jsp">Browse</a>
										</li>
									</ul>
								</div>
							</td>
							<td width="20"></td>
							<td align="center">		
								<form  method="post">
									<table border="0" cellspacing="0" cellpadding="0">
										<tr height= 5></tr>
										<tr>
											<td align="right"> Knowledge Base Name: &nbsp;</td>
											<td height=35><input type="text" name="name" size=50 ></td>
										</tr>
										<tr>
											<td align="right"> Description: &nbsp;</td>
											<td height=35><input type="text" name="description"  size=50></td>
										</tr>
										<tr>
											<td align="right"> Domain / Specialty:&nbsp; </td>
											<td height=35> <input type="text" name="domain" size=50></td>
										</tr>
										<tr>
											<td>&nbsp;</td>
											<td>&nbsp;</td>
										</tr>
										<tr>
											<td>&nbsp;</td>
											<td align="right"><input type="submit" name="B1" value="Next Step"></td>
										</tr>
									</table>
								</form>
							</td>
						</tr>
					</table>
				</td>		
			</tr>
		</table>
	</center>

  <jsp:useBean id="DBConnectBean" scope="session" class="edu.utah.bmi.ckass.bean.DBConnectBean" >
  </jsp:useBean>
  
<%
	String name ="";
	String value="";    
	Enumeration <String> e = request.getParameterNames();

	while (e.hasMoreElements()) {
    	name = e.nextElement();
        value = request.getParameter(name);
        session.setAttribute(name, value);
    }
    
    String tname = request.getParameter("name");
    String tdesc = request.getParameter("description");
    String tdomain = request.getParameter("domain");    
    
    if ( ! ((tname == null) || ( tname.isEmpty()))) {
    	String sql="Insert into ckass.task (uid, name, description, domain, date) values (" + Integer.toString(uid) +", '" +
	            tname+"', '"+tdesc+"','" + tdomain + "', now() " + ")";
		int i=DBConnectBean.executeUpdate(sql);
		
		String sql_getTID = "select tid from ckass.task where name='" + tname + "'";
		ResultSet RSS =DBConnectBean.executeQuery(sql_getTID);
		
		int tid=0;
		
		while (RSS.next()) { 
			tid = RSS.getInt("tid");
		}
		
		if (tid>0){
			session.setAttribute("tid", tid);
		}else {
			out.println("New Task: " + "Error in retrieving the task ID!");
		}
		
		response.sendRedirect("ConceptResult.jsp");
    }
%>


</body>
</html>