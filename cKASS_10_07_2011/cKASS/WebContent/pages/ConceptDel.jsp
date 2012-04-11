<%@ page language="java" import="java.util.*,java.sql.*" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%
  //String username=(String)session.getAttribute("username");
  int uid=(Integer)session.getAttribute("uid");
  int tid=(Integer)session.getAttribute("tid");
%>
  <jsp:useBean id="DBConnectBean" scope="session" class="edu.utah.bmi.ckass.bean.DBConnectBean" >
  </jsp:useBean>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<%
    Enumeration del = request.getParameterNames();
    while (del.hasMoreElements()) {
        String name = (String)del.nextElement();
        int value = Integer.parseInt(request.getParameter(name).toString());
        String sql="Delete from ckass.concept where concept_no="+value;
        int i=DBConnectBean.executeUpdate(sql);
        //out.println(sql);
    } 
     response.sendRedirect("ConceptResult.jsp");
%>
</body>
</html>