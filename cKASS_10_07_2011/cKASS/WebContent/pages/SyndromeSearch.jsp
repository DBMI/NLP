<%@ page import="java.sql.*, com.hp.hpl.jena.sdb.*, java.util.*, com.hp.hpl.jena.query.*, com.hp.hpl.jena.sdb.SDBException" language="java"
	contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%
	//String username = (String) session.getAttribute("username");
%>
  <jsp:useBean id="JenaSDBConnectBean" scope="session" class="edu.utah.bmi.ckass.sparql.JenaSDBConnectBean" >
  </jsp:useBean>
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
										<li><a href="CreateOntology.jsp">Create KB</a></li>
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
														<td width="300" align="left">Syndrome: <select name="Syndrome_category">
                <option value=1>InfluenzaLikeIllness Syndrome</option>
                <option value=2>Constitutional Syndrome</option>
                <option value=3>Botulism Syndrome</option>
                <option value=4>Hemorrhagic Syndrome</option>
                <option value=5>Gastrointestinal Syndrome</option>
                <option value=6>Neurological Syndrome</option>
                <option value=7>Rash Syndrome</option>
                <option value=8>Respiratory Syndrome</option>
                </select> 
														</td>
														<td align=center width="70"><input type="image"
															src="../images/search.png" width="30" height="25"
															name="search" />
														</td></tr>
													<tr height="30"></tr>	
													<tr><td><input type=submit value="Add concepts to my KB" ></td></tr>	
													
													<tr height="30"></tr>
												</table>
												<table bgcolor="#f1f1f1" border="1" cellspacing="1">


													<%
														//String syndrome_category = request.getParameter("Syndrome_category");
													    //int syndrome_category_num= Integer.parseInt(syndrome_category);
													    int syndrome_category_num= 1;
														if (syndrome_category_num==1) {
															String sql_syndrome = "SELECT ?o {?s ?p ?o FILTER ( regex(?s, 'botulismSyndrome') )}";

															ArrayList<String> RS_syndrome = JenaSDBConnectBean
																	.excuteQuery(sql_syndrome);
															int i=0;
															while (i<RS_syndrome.size()) {
																i++;			
													%>
													<tr>
														<td><INPUT type=checkbox name="concept_syndrome" value=null></td>
														<td><%=RS_syndrome.get(i)%></td>
													</tr>
													<%
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