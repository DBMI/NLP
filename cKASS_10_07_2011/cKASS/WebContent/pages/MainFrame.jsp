<%@ page import="java.sql.*" language="java"
	contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%
	String username = (String) session.getAttribute("username");
	int uid = (Integer) session.getAttribute("uid");
%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>My Workspace</title>
<link href="../style/style.css" type="text/css" rel="stylesheet" />
</head>
<body>
	<center>
		<table  >
			<tr>
				<td>
					<table>
						<tr>
							<td><img src="../images/header_ban.png"></td>
						</tr>
					</table>
				</td>
			</tr>
			<tr>
				<td align="left">
					<table>
						<tr>
							<td valign="top">
								<div id="navigation">
									<ul>
										<li><a href="MainFrame.jsp">My WorkSpace</a>
										</li>
										<li><a href="CreateOntology.jsp">Create KB</a>
										</li>
										<li><a href="PublicKBs.jsp">Community Space</a>
										</li>
										<li><a href="Search.jsp">Search</a>
										</li>
										<li><a href="Browse.jsp">Browse</a>
										</li>
									</ul>
								</div>
							</td>
							<td width=30></td>
							<td align="center">

								<form action="ConceptResult.jsp" method=GET>
									<TABLE bordercolor="#f1f1f1" border=1 width=670 align=center>
										<CAPTION >
											<b> <%= username %>'s Workspace</b>
										</CAPTION>
										<tr height="15"></tr>
										<tr align="center">
											<th>&nbsp;</th>
											<th>NAME</th>
											<th>DESCRIPTION</th>
											<th>DOMAIN</th>
											<th>CREATED</th>
											<th>STATUS</th>
										</tr>
										<jsp:useBean id="DBConnectBean" scope="session"
											class="edu.utah.bmi.ckass.bean.DBConnectBean">
										</jsp:useBean>

										<%
											//String cid="";
											//String cname="";
											int tid = 0;
											String sql = "SELECT * FROM ckass.task where uid=" + uid;
											ResultSet RS = DBConnectBean.executeQuery(sql);

											while (RS.next()) {
												//cid=RS.getString("c_id");
												//cname=RS.getString("c_name");
												tid = RS.getInt("tid");
										%>
										<tr align="center">
											<td><INPUT type=radio name="tid" value=<%=tid%>>
											<td><%=RS.getString("name")%></td>
											<td><%=RS.getString("description")%></td>
											<td><%=RS.getString("domain")%></td>
											<td><%=RS.getString("date")%></td>
											<td><% if (RS.getBoolean("status")){ %> Published
											     <% } else {%>In progress <% }%>
											</td>
										</tr>
										<%
											}
											RS.close();
										%>
									</TABLE>
									<%
										if (tid != 0) {
									%>
									<p>
										&nbsp;&nbsp; <input type=submit value="Enter Knowledge Base">&nbsp;&nbsp;
										<%
											}
										%>
									
								</form>
								<p>
							</td>
						</tr>
					</table></td>
			</tr>
		</table>
	</center>

</body>
</html>