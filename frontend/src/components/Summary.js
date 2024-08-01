import { useState, useEffect } from "react";
import InvestorsTable from "./InvestorsTable";
import CommitmentsTable from "./CommitmentsTable";

export default function Summary() {
    const [selectedInvestor, setSelectedInvestor] = useState(null);
    
    return (
        <div className="investor-summary">
            <InvestorsTable selectedInvestor={selectedInvestor} setSelectedInvestor={setSelectedInvestor}/>
            <CommitmentsTable selectedInvestor={selectedInvestor}/>
        </div>
    );
}