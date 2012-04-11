<%@ page language="java" import="java.sql.*" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%
  //String username=(String)session.getAttribute("username");
  int uid=(Integer)session.getAttribute("uid");
  int tid=(Integer)session.getAttribute("tid");
%>

<script language="javascript">
function FnRefresh()
{
   opener.location.reload();
}
function check()
{
if(document.add.ConceptNameAdd.value.length==0){
     alert("Concept cannot be null!");
     document.add.ConceptNameAdd.focus();
     return false;
    }
  }
</script>    
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Add new Concept</title>
<link href="../style/style.css" type="text/css" rel="stylesheet" />
</head>
<body onunload=FnRefresh() >

<table>

    <caption> </caption>
    <tbody>
    <form action="AddConcept.jsp" name="add" method="post" onsubmit="return check()">
        <tr>
            <td>Which type of concept you want to add:&nbsp;&nbsp;<select name="concept_category">
                <option value=1>Medication</option>
                <option value=2>Sign/Symptom</option>
                <option value=3>Anatomical Sites</option>
                <option value=4>Disease/Disorder</option>
                <option value=5>Procedure</option>
                <option value=6>Lab</option>
                </select> 
            </td>
        </tr>
        <tr>
            <td align="left">Concept:&nbsp;&nbsp;<input type='text' name="ConceptNameAdd">
            </td>
        </tr>
        <tr>
            <td><input type=submit value="Add"></td>
        </tr></form>
    </tbody>
</table>
<p>&nbsp;</p>
  <jsp:useBean id="DBConnectBean" scope="session" class="edu.utah.bmi.ckass.bean.DBConnectBean" >
  </jsp:useBean>
<%
       String nameAdd=request.getParameter("ConceptNameAdd");
       String concept_category=request.getParameter("concept_category");
       //out.println(nameAdd);
       //out.print(concept_category);
       if (concept_category != null ) {
       int concept_category_num= Integer.parseInt(concept_category);
       String sql="Insert into ckass.concept (name,category_no,date,uid,tid) values ('"+
                  nameAdd+"',"+concept_category_num+", now(),"+uid+","+tid+")";
       int i=DBConnectBean.executeUpdate(sql);
       //out.println(sql);
       }
       
%>

</body>
</html>