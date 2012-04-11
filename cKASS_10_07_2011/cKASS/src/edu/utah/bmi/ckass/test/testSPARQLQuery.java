package edu.utah.bmi.ckass.test;

import java.util.ArrayList;

import com.hp.hpl.jena.query.QuerySolution;
import com.hp.hpl.jena.query.ResultSet;
import com.hp.hpl.jena.query.ResultSetFormatter;

import edu.utah.bmi.ckass.bean.*;
import edu.utah.bmi.ckass.sparql.JenaSDBConnectBean;

public class testSPARQLQuery {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		JenaSDBConnectBean jenaConnect = new JenaSDBConnectBean();
		ArrayList <String> rs = jenaConnect.excuteQuery("SELECT ?o {?s ?p ?o FILTER ( regex(?s, 'botulismSyndrome') )}");
		
		for (int i =0; i < rs.size(); i ++){
			System.out.println(rs.get(i));	
		}

	}
}
