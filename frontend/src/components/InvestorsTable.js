import { useState, useEffect } from "react";
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Grid, TablePagination } from "@mui/material";
import Typography from '@mui/material/Typography';
import { format } from "date-fns";
import numeral from 'numeral';

export default function InvestorsTable({ selectedInvestor, setSelectedInvestor}) {
    const [investors, setInvestors] = useState([]);
    const [loading, setLoading] = useState(true);
    
    useEffect(() => {
        fetch('/api/v1/investors')
        .then(response => response.json())
        .then(data => {
            setInvestors(data.investors);
            setLoading(false);
        });
    }, []);
    
    return (
        <>
        {loading ? (
          <div>Loading...</div>
        ) : (
          <Grid container direction="column" justifyContent="center" alignItems="center" sx={{ mb: 8, mt: 2}}>
            <Typography variant="h5" gutterBottom component="div">
              Investors
            </Typography>
            <Paper sx={{ m: 1}}>
              <TableContainer component={Paper}>
                <Table sx={{ minWidth: 800 }} aria-label="Investors" size="small">
                  <TableHead>
                    <TableRow>
                      <TableCell>Id</TableCell>
                      <TableCell align="left">Name</TableCell>
                      <TableCell align="left">Type</TableCell>
                      <TableCell align="left">Date Added</TableCell>
                      <TableCell align="left">Address</TableCell>
                      <TableCell align="left">Total Commitment</TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {investors
                      .map((row) => (
                        <TableRow
                          key={row.id}
                          sx={{ '&:last-child td, &:last-child th': { border: 0 }, backgroundColor: selectedInvestor.id === row.id ? 'rgba(0, 0, 255, 0.1)' : 'inherit'  }}
                          hover
                        //   selected={seletectedTitle["id"] === row["id"]}
                          onClick={() => setSelectedInvestor(row)}
                        >
                          <TableCell component="th" scope="row">
                              {row["id"]}
                          </TableCell>
                          <TableCell align="left">{row.name}</TableCell>
                          <TableCell align="left">{row.investory_type}</TableCell>
                          <TableCell align="left">{format(row.created_at, "MMMM d, yyyy")}</TableCell>
                          <TableCell align="left">{row.address}</TableCell>
                          <TableCell align="left">{'£' + numeral(row.total_commitment).format('0.0a')}</TableCell>
                        </TableRow>
                      ))}
                  </TableBody>
                </Table>
              </TableContainer>
            </Paper>
          </Grid>
        )}
      </>
    );
    }