package edu.utah.bmi.ckass.test;

import java.io.InputStream;

import com.hp.hpl.jena.query.Query;
import com.hp.hpl.jena.query.QueryExecution;
import com.hp.hpl.jena.query.QueryExecutionFactory;
import com.hp.hpl.jena.query.QueryFactory;
import com.hp.hpl.jena.query.ResultSet;
import com.hp.hpl.jena.query.ResultSetFormatter;
import com.hp.hpl.jena.rdf.model.Model;
import com.hp.hpl.jena.rdf.model.ModelFactory;
//

public class sparqlengine {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		String queryString= "select ?x ?label where { ?x <http://www.w3.org/2000/01/rdf-schema#label> ?label}";
		String url= "http://ss-ontology.googlecode.com/svn/trunk/skos/esso.xml";

		Model model= ModelFactory.createDefaultModel().read(url, "N-TRIPLES");
		Query query=QueryFactory.create(queryString);
		QueryExecution qexec = QueryExecutionFactory.create(query, model);
		ResultSet results = qexec.execSelect();

		ResultSetFormatter.out(results);
		
		while (results.hasNext()) {
//		    QuerySolution row= results.next();
//		    RDFNode thing= row.get("x")
//		    Literal label= row.getLiteral("label");
//		    System.out.println(x.toString()+" is named "+label.getString());
		}
		
	}

}
