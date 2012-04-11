<%@ page language="java" import="java.sql.*,java.util.*" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>

<%
  String username=(String)session.getAttribute("username");
  int uid=(Integer)session.getAttribute("uid"); 
%>
<%
    //ResultSet RS = null;
    Enumeration e = request.getParameterNames();
    while (e.hasMoreElements()) {
        String name = (String)e.nextElement();
        int value = Integer.parseInt(request.getParameter(name).toString());
        session.setAttribute(name, value);
    } 
%>
<%
  int tid=(Integer)session.getAttribute("tid");
%>
<script LANGUAGE="JavaScript">

function openwin(){
	window.open("AddConcept.jsp", "newwindow", "left=550, top=550, height=200, width=400");
}

</script>


<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>ListConcept</title>
<link href="../style/style.css" type="text/css" rel="stylesheet" />
</head>
<body >
<center>
<table>
<tr>
<td>
<table>
<tr>

<td>
<img src="../images/header_ban.png" >
</td>
</tr>
</table>
</td>
</tr>
<tr>
    <td align="left" ><table>
<tr>
<td valign="top"><div id="navigation">
<ul >
<li><a href="MainFrame.jsp">My WorkSpace</a>
										</li>
										<li><a href="CreateOntology.jsp">Create KnowledgeBase</a>
										</li>
										<li><a href="Search.jsp">Search</a>
										</li>
										<li><a href="Browse.jsp">Browse</a>
										<li><a href="Export.jsp"  >Export</a>
</ul>					
</div>
</td>
<td align="center">
<jsp:useBean id="DBConnectBean" scope="session" class="edu.utah.bmi.ckass.bean.DBConnectBean" >
</jsp:useBean>
<form action="ConceptDel.jsp" method="post">
<table width="600px" >
    <tbody>
        <tr>
            <td width="50%" valign="top">
            <table   width="250px" frame="vsides" border="1px">
                <caption>Medication</caption>
                <tbody>
                     
<%
	int concept_no_med=0;
    String concept_name_med=null;
    String sql_med="SELECT * FROM ckass.concept where tid="+tid+" and category_no=1";
    //out.println(sql);
    ResultSet RSS_med =DBConnectBean.executeQuery(sql_med);   
	while (RSS_med.next()) { 
	//cid=RSS.getString("c_id");
    //cname=RSS.getString("c_name");
    concept_no_med=RSS_med.getInt("concept_no");
    concept_name_med= "Concept_no"+RSS_med.getString("concept_no");
%>
    <tr align="center">
    <td width="50px"><INPUT type=checkbox name=<%=concept_name_med%> value=<%=concept_no_med%> >
    <td><%=RSS_med.getString("name")%></td>
    </tr>
<%
	}
RSS_med.close();
%>

                </tbody>
            </table>
            </td>
            <td valign="top">
            <table border="1" width="250px">
                <caption>Sign/Symptom</caption>
                <tbody>
<%
	int concept_no_sym=0;
    String concept_name_sym=null;
    String sql_sym="SELECT * FROM ckass.concept where tid="+tid+" and category_no=2";
    ResultSet RSS_sym =DBConnectBean.executeQuery(sql_sym);   
	while (RSS_sym.next()) { 
    concept_no_sym=RSS_sym.getInt("concept_no");
    concept_name_sym= "Concept_no"+RSS_sym.getString("concept_no");
%>
    <tr align="center">
    <td width="50px"><INPUT type=checkbox name=<%=concept_name_sym%> value=<%=concept_no_sym%> >
    <td><%=RSS_sym.getString("name")%></td>
    </tr>
<%
	}
RSS_sym.close();
%>
                </tbody>
            </table>
            </td>
        </tr>
        <tr>
            <td valign="top">
            <table border="1" width="250px">
                <caption>Anatomical sites</caption>
                <tbody>
<%
	int concept_no_anat=0;
    String concept_name_anat=null;
    String sql_anat="SELECT * FROM ckass.concept where tid="+tid+" and category_no=3";
    ResultSet RSS_anat =DBConnectBean.executeQuery(sql_anat);   
	while (RSS_anat.next()) { 
    concept_no_anat=RSS_anat.getInt("concept_no");
    concept_name_anat= "Concept_no"+RSS_anat.getString("concept_no");
%>
    <tr align="center">
    <td width="50px"><INPUT type=checkbox name=<%=concept_name_anat%> value=<%=concept_no_anat%> >
    <td><%=RSS_anat.getString("name")%></td>
    </tr>
<%
	}
RSS_anat.close();
%>
                </tbody>
            </table>
            </td>
            <td valign="top">
            <table border="1" width="250px">
                <caption>Disease/Disorder</caption>
                <tbody>
<%
	int concept_no_dx=0;
    String concept_name_dx=null;
    String sql_dx="SELECT * FROM ckass.concept where tid="+tid+" and category_no=4";
    ResultSet RSS_dx =DBConnectBean.executeQuery(sql_dx);   
	while (RSS_dx.next()) { 
    concept_no_dx=RSS_dx.getInt("concept_no");
    concept_name_dx= "Concept_no"+RSS_dx.getString("concept_no");
%>
    <tr align="center">
    <td width="50px"><INPUT type=checkbox name=<%=concept_name_dx%> value=<%=concept_no_dx%> >
    <td><%=RSS_dx.getString("name")%></td>
    </tr>
<%
	}
RSS_dx.close();
%>
                </tbody>
            </table>
            </td>
        </tr>
        <tr>
            <td valign="top" >
            <table border="1" width="250px">
                <caption>Procedure</caption>
                <tbody>
<%
	int concept_no_proc=0;
    String concept_name_proc;
    String sql_proc="SELECT * FROM ckass.concept where tid="+tid+" and category_no=5";
    ResultSet RSS_proc =DBConnectBean.executeQuery(sql_proc);   
	while (RSS_proc.next()) { 
    concept_no_proc=RSS_proc.getInt("concept_no");
    concept_name_proc= "Concept_no"+RSS_proc.getString("concept_no");
%>
    <tr align="center">
    <td width="50px"><INPUT type=checkbox name=<%=concept_name_proc%> value=<%=concept_no_proc%> >
    <td><%=RSS_proc.getString("name")%></td>
    </tr>
<%
	}
RSS_proc.close();
%>
                </tbody>
            </table>
            </td>
            <td valign="top">
            <table border="1" width="250px">
                <caption>Lab</caption>
                <tbody>
<%
	int concept_no_lab=0;
    String concept_name_lab=null;
    String sql_lab="SELECT * FROM ckass.concept where tid="+tid+" and category_no=6";
    ResultSet RSS_lab =DBConnectBean.executeQuery(sql_lab);   
	while (RSS_lab.next()) { 
    concept_no_lab=RSS_lab.getInt("concept_no");
    concept_name_lab= "Concept_no"+RSS_lab.getString("concept_no");
%>
    <tr align="center">
    <td width="50px"><INPUT type=checkbox name=<%=concept_name_lab%> value=<%=concept_no_lab%> >
    <td><%=RSS_lab.getString("name")%></td>
    </tr>
<%
	}
RSS_lab.close();
%>
                </tbody>
            </table>
            </td>
        </tr>
        <tr>
            <td><br><br><input type=submit value="Delete selected concepts"></td>
            <td>
            <br><br>
            <input type=button onclick="openwin()" value="Add new concept" >
            </td>
            
        </tr>
    </tbody>
</table>
</form>
</td>
</tr>
</table>
</td>
</tr>
</table>
</center>

</body>
</html>
