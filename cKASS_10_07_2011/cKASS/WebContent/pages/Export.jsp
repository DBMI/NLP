<%@ page language="java"  import="java.io.*,java.sql.*,java.util.Date, java.text.SimpleDateFormat" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>

<%
response.setContentType("text/csv");
response.setHeader("Content-Disposition", "attachment; filename=knowledgebase.csv");
%>
<%
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
SimpleDateFormat sdf_new = new SimpleDateFormat("dd-MM-yyyy");
String date = sdf_new.format(new Date());

//String path = pageContext.getServletContext().getRealPath("/export.jsp");
//out.print(path);
//String filename = path+"WebContent\\data\\KB_";
String filename = "d:\\KB_"; //this path need to change when installed on server. I have trouble in using relative path.
filename += date;
filename += "_";
filename += uid;
filename +="_";
filename += tid;
filename += ".csv";
out.print(filename);


try
{

FileWriter fw = new FileWriter(filename);
fw.append("Concept_no");
fw.append(',');
fw.append("Concept_name");
fw.append(',');
fw.append("category");
fw.append('\n');


String sql_export = "select c.concept_no, c.name, v.string from ckass.concept c, ckass.vocab v where v.type_no=c.category_no and c.tid="
                    +tid;
ResultSet RS_export =DBConnectBean.executeQuery(sql_export);
while(RS_export.next())
{
fw.append(Integer.toString((RS_export.getInt("concept_no"))));
fw.append(',');
fw.append(RS_export.getString("name"));
fw.append(',');
fw.append(RS_export.getString("string"));
fw.append('\n');
}
fw.flush();
fw.close();
RS_export.close();
out.println("<b>You are Successfully Created Csv file.</b>");
} catch (Exception e) {
e.printStackTrace();
}
%>


</body>
</html>
