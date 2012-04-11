<%@ page import="java.util.*" language="java"
	contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

<html>
<head>
<title>getParameterNames() method of request object.</title>
</head>
<body>
	<form method="post">
		<table border="0" cellspacing="0" cellpadding="0">
			<tr>
				<td align="right">Dictionary/Ontology Name:</td>
				<td><input type="text" name="tskname" size=50>
				</td>
			</tr>
			<tr>
				<td align="right">Description:</td>
				<td><input type="text" name="tskdesc" size=50>
				</td>
			</tr>
			<tr>
				<td align="right">Domain / Specialty:</td>
				<td><input type="text" name="tskdomain" size=50>
				</td>
			</tr>
			<tr>
				<td>&nbsp;</td>
				<td>&nbsp;</td>
			</tr>
			<tr>
				<td>&nbsp;</td>
				<td align="right"><input type="submit" name="B1"
					value="Create Task">
				</td>
			</tr>
		</table>
	</form>
	<%
		String ParameterNames = "";
		for (Enumeration e = request.getParameterNames(); e
				.hasMoreElements();) {
			ParameterNames = (String) e.nextElement();
			out.println(ParameterNames + "<br/>");
			String value = request.getParameter(ParameterNames);
			out.println(value + "<br/>");
		}
	%>
</body>
</html>