<%@ page import="java.sql.*" language="java"
	contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%
	String username = (String) session.getAttribute("username");
	Integer uid = (Integer) session.getAttribute("uid");
%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>MainFrame</title>
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
							<td><img src="../images/header_ban.png"></td>
						</tr>
					</table></td>
			</tr>
			<tr>
				<td align="right" > User Name:<%=username%>
				</td>
			</tr>
			<tr>
				<td align="left">
					<table>
						<tr>
							<td>
								<div id="navigation">
									<ul>
										<li><a href="MainFrame.jsp">My Dictionary</a>
										</li>
										<li><a href="Browse.jsp">Query Concept</a>
										</li>
										<li><a href=""  >Public Dictionary</a>
										</li>
										<li><a href="?">?</a>
										</li>
									</ul>
								</div>
							</td>	
							<td>
								<table>
									<tr>
										<td>
											<form method="get" action=BrowseConcept.jsp>
												<input type="text" name="searchConcept" />
												<input type="image" src="../images/search.png" width="30" height="25" name="search"/>
											</form>
										</td>
									</tr>
								</table>
							</td>					
						</tr>
					</table>
				</td>	
			</tr>
			<tr>
				<td>
					<form action="AddConcept.jsp" method="get">
						<input type=submit value="Add concept">
					</form>
				</td>
			</tr>
		</table>
	</center>

</body>
</html>