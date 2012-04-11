package edu.utah.bmi.ckass.sparql;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Iterator;

import com.hp.hpl.jena.query.Dataset;
import com.hp.hpl.jena.query.Query;
import com.hp.hpl.jena.query.QueryExecution;
import com.hp.hpl.jena.query.QueryExecutionFactory;
import com.hp.hpl.jena.query.QueryFactory;
import com.hp.hpl.jena.query.QuerySolution;
import com.hp.hpl.jena.query.ResultSet;
import com.hp.hpl.jena.query.ResultSetFormatter;
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

public class JenaSDBConnectBean {

	public Connection jdbc = null;
	public String jdbcURL = "jdbc:mysql://localhost:3306/jenasdb";
	public StoreDesc storeDesc; 
	
	public JenaSDBConnectBean() {
		
		//connect the triple store
		storeDesc = new StoreDesc (LayoutType.LayoutTripleNodesHash, DatabaseType.MySQL);
		storeDesc.engineType = MySQLEngineType.InnoDB;		

	}
	
	public ArrayList <String> excuteQuery( String queryString) {
		   
		JDBC.loadDriverMySQL() ;
			
		try {			
			jdbc =  DriverManager.getConnection(jdbcURL, "root","123456") ;
		} catch (SQLException ex)
		{
           throw new SDBException("SQL Exception while connecting to database: "+jdbcURL+" : "+ex.getMessage()) ;
		}
	   
        Query query = QueryFactory.create(queryString) ;

        SDBConnection conn = new SDBConnection(jdbc) ;
        
        Store store = StoreFactory.create(storeDesc, conn) ;
//	        Model model = SDBFactory.connectDefaultModel(store) ;
        
        Dataset ds = SDBFactory.connectDataset(conn, storeDesc);
        QueryExecution qe = QueryExecutionFactory.create(query, ds) ;
        
        ArrayList <String> rsList = new ArrayList <String>(); 
        
        ResultSet rs = null;

        try {
            rs = qe.execSelect() ;
            
    		while (rs.hasNext()){
    			QuerySolution rsSub = rs.next();
    			String subResource = rsSub.getResource("o").toString();
    			if (subResource.indexOf("resource#") > 0){
    				rsList.add( subResource.split("#")[1]);
    			}    			
    		}
////            ResultSetFormatter.out(rs) ;
//           String xmlRslt = ResultSetFormatter.asXMLString(rs) ;
        } catch(Throwable t) {
        	t.printStackTrace();
        }
        finally { 
        	qe.close() ;
        }
        // Does not close the JDBC connection.
        // Do not call : store.getConnection().close() , which does close the underlying connection.
        store.close() ;
        
        return rsList;
    }
	
}
