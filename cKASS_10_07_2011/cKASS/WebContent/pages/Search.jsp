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
<title>Search Concept</title>
<link href="../style/style.css" type="text/css" rel="stylesheet" />
</head>
<body>
	<center>
		<table>
			<tr>
				<td>
					<table>
						<tr>
							<td><img src="../images/header_ban.png">
							</td>
						</tr>
					</table></td>
			</tr>
			<tr>
				<td align="left" >
					<table>
						<tr>
							<td valign="top">
								<div id="navigation">
									<ul>
										<li><a href="MainFrame.jsp">My WorkSpace</a></li>
										<li><a href="CreateOntology.jsp">Create KnowledgeBase</a></li>
										<li><a href="Search.jsp">Search</a></li>
										<li><a href="Browse.jsp">Browse</a></li>
									</ul>
								</div>
							</td>
							<td>
								<table width="600px">
									<tr>
										<td>
											<form method="get">
												<table>
													<tr>
														<td width="180" align="right"><input type="text"
															name="cname" width=30 />
														</td>
														<td align=center width="70"><input type="image"
															src="../images/search.png" width="30" height="25"
															name="search" />
														</td>
													</tr>
													<tr height="30"></tr>
												</table>
												<table bgcolor="#f1f1f1" border="1" cellspacing="1">
													<jsp:useBean id="DBConnectBean" scope="session"
														class="edu.utah.bmi.ckass.bean.DBConnectBean">
													</jsp:useBean>

													<%
														String concept = request.getParameter("cname");
														if (!((concept == null) || (concept.isEmpty()))) {
															String sql_conceptInfo = "select n2.lex as prd, n3.lex as obj "
																	+ "from jenasdb.nodes n1, jenasdb.nodes n2, jenasdb.nodes n3, jenasdb.triples t"
																	+ " where t.s=n1.hash AND t.p=n2.hash AND t.o=n3.hash"
																	+ " AND n1.lex like '%" + concept
																	+ "%' AND n2.lex like '%core#%'";

															System.out.println(sql_conceptInfo);
															ResultSet RSS_conceptInfo = DBConnectBean
																	.executeQuery(sql_conceptInfo);
															
															int count=0;
															while (RSS_conceptInfo.next()) {
																count ++;
																if (count==1){
																	%>
														<thead>
															<tr>
																<th>PROPERTY</th>
																<th>VALUE</th>
															</tr>
														</thead>
															<%
																}
																String pStr = RSS_conceptInfo.getString("prd");
																String[] pStrArr;
																if (pStr.indexOf("#") > 0) {
																	pStrArr = pStr.split("#");
													%>
													<tr>
														<td><%=pStrArr[1]%></td>
														<td><%=RSS_conceptInfo.getString("obj")%></td>
													</tr>
													<%
														}
															}
														}
													%>

												</table>
											</form>
										</td>
									</tr>
								</table>
							</td>


						</tr>
					</table></td>
			</tr>
		</table>
	</center>

</body>
</html>