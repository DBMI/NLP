package edu.utah.bmi.ckass.sparql;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

import com.hp.hpl.jena.query.*;
import com.hp.hpl.jena.rdf.model.Model;
import com.hp.hpl.jena.rdf.model.Statement;
import com.hp.hpl.jena.rdf.model.StmtIterator;
import com.hp.hpl.jena.sdb.SDBException;
import com.hp.hpl.jena.sdb.SDBFactory;
import com.hp.hpl.jena.sdb.Store;
import com.hp.hpl.jena.sdb.StoreDesc;
import com.hp.hpl.jena.sdb.sql.JDBC;
import com.hp.hpl.jena.sdb.sql.MySQLEngineType;
import com.hp.hpl.jena.sdb.sql.SDBConnection;
import com.hp.hpl.jena.sdb.store.DatabaseType;
import com.hp.hpl.jena.sdb.store.LayoutType;
import com.hp.hpl.jena.sdb.store.StoreFactory;

public class QueryFromStore {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String queryString = "SELECT ?s ?p ?o {?s ?p ?o FILTER ( regex(?s, 'botulismSyndrome') )}";
		
		//Query query = QueryFactory.create(queryString);
		 
		//connect the triple store
		StoreDesc storeDesc = new StoreDesc (LayoutType.LayoutTripleNodesHash, DatabaseType.MySQL);
		storeDesc.engineType = MySQLEngineType.InnoDB;
		
		JDBC.loadDriverMySQL() ;

		String jdbcURL = "jdbc:mysql://localhost:3306/jenasdb";
		Connection jdbc ;
		try {			
			jdbc =  DriverManager.getConnection(jdbcURL, "root","123456") ;
		} catch (SQLException ex)
		{
           throw new SDBException("SQL Exception while connecting to database: "+jdbcURL+" : "+ex.getMessage()) ;
		}
		
        // Make some calls to the store, using the same JDBC connection and store description.
 
        query( queryString, storeDesc, jdbc) ;
        
//        System.out.println("Predicates: ") ;
//        query("SELECT DISTINCT ?p { ?s ?p ?o }", storeDesc, jdbc) ;
//        System.out.println("Objects: ") ;
//        query("SELECT DISTINCT ?o { ?s ?p ?o }", storeDesc, jdbc) ;
		
	}

	   public static void query( String queryString, StoreDesc storeDesc, Connection jdbcConnection)
	   {
	        Query query = QueryFactory.create(queryString) ;

	        SDBConnection conn = new SDBConnection(jdbcConnection) ;
	        
	        Store store = StoreFactory.create(storeDesc, conn) ;
//	        Model model = SDBFactory.connectDefaultModel(store) ;
	        
	        Dataset ds = SDBFactory.connectDataset(conn, storeDesc);
	        QueryExecution qe = QueryExecutionFactory.create(query, ds) ;
	        
	        try {
	            ResultSet rs = qe.execSelect() ;
//	            System.out.println("***** Result set: " + rs);
	            
	            while(rs.hasNext()){
	            	QuerySolution qs = rs.next();
	            	System.out.println(qs.toString());
	            }
	            ResultSetFormatter.out(rs) ;
          
	        } catch(Throwable t) {
	        	t.printStackTrace();
	        }
	        finally { 
	        	qe.close() ;
	        }
	        // Does not close the JDBC connection.
	        // Do not call : store.getConnection().close() , which does close the underlying connection.
	        store.close() ;
	    }
	   
}
