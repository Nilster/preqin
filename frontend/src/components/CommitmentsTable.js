import { useState, useEffect } from "react";
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Grid } from "@mui/material";
import Typography from '@mui/material/Typography';
import numeral from 'numeral';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Box from '@mui/material/Box';

export default function CommitmentsTable({ selectedInvestor }) {
  const [clientCommitments, setClientCommitments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [assetClass, setAssetClass] = useState("hedge_funds");

  useEffect(() => {
    if (selectedInvestor) {
      fetch(`/api/v1/commitments?investor_id=${selectedInvestor.id}`)
        .then(response => response.json())
        .then(data => {
          setClientCommitments(data);
          setLoading(false);
          setAssetClass('all');
        });
    }
  }, [selectedInvestor]);

  const handleAssetClassChange = (event, newValue) => {
    setAssetClass(newValue);
  }

  return (
    <>
      {loading ? (
        <div>Loading...</div>
      ) : (
        <Grid container direction="column" justifyContent="center" alignItems="center">
          <Typography variant="h5" gutterBottom component="div">
            Commitments
          </Typography>
          <Grid container direction="row" justifyContent="center" alignItems="center">
            <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
              <Tabs value={assetClass} onChange={handleAssetClassChange} aria-label="asset-class-tabs">
                <Tab value="all" label={
                  <Box>
                    <Typography variant="caption" component="pre">All</Typography>
                    <Typography variant="title">£{numeral(clientCommitments.total_commitment).format('0.0a')}</Typography>
                  </Box>
                } />
                <Tab value="hedge_funds" label={
                  <Box>
                    <Typography variant="caption" component="pre">Hedge Funds</Typography>
                    <Typography variant="title">£{numeral(clientCommitments.hedge_funds.class_total).format('0.0a')}</Typography>
                  </Box>
                } />
                <Tab value="private_equity" label={
                  <Box>
                    <Typography variant="caption" component="pre">Private Equity</Typography>
                    <Typography variant="title">£{numeral(clientCommitments.private_equity.class_total).format('0.0a')}</Typography>
                  </Box>
                } />
                <Tab value="real_estate" label={
                  <Box>
                    <Typography variant="caption" component="pre">Real Estate</Typography>
                    <Typography variant="title">£{numeral(clientCommitments.real_estate.class_total).format('0.0a')}</Typography>
                  </Box>
                } />
                <Tab value="infrastructure" label={
                  <Box>
                    <Typography variant="caption" component="pre">Infrastructure</Typography>
                    <Typography variant="title">£{numeral(clientCommitments.infrastructure.class_total).format('0.0a')}</Typography>
                  </Box>
                } />
                <Tab value="natural_resources" label={
                  <Box>
                    <Typography variant="caption" component="pre">Natural Resources</Typography>
                    <Typography variant="title">£{numeral(clientCommitments.natural_resources.class_total).format('0.0a')}</Typography>
                  </Box>
                } />
              </Tabs>
            </Box>
          </Grid>
          <Paper sx={{ m: 1 }}>
            <TableContainer component={Paper} style={{ maxHeight: 400, overflowY: 'auto' }}>
              <Table sx={{ minWidth: 800 }} aria-label="Commitments" size="small" stickyHeader>
                <TableHead>
                  <TableRow>
                    <TableCell>Id</TableCell>
                    <TableCell align="left">Asset Class</TableCell>
                    <TableCell align="left">Currency</TableCell>
                    <TableCell align="left">Amount</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {
                    Object.entries(clientCommitments)
                      .filter(([k, v]) => {
                        if (assetClass === 'all') {
                          return v.commitments
                        } else {
                          return k === assetClass
                        }
                      })
                      .map(([k, v]) => {
                        return v.commitments.map((row) => (
                          <TableRow
                            key={row.id}
                            sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                            hover>
                            <TableCell component="th" scope="row">
                              {row["id"]}
                            </TableCell>
                            <TableCell align="left">{row.asset_class}</TableCell>
                            <TableCell align="left">{row.currency}</TableCell>
                            <TableCell align="left">{'£' + numeral(row.amount).format('0.0a')}</TableCell>
                          </TableRow>
                        ))
                      })
                  }

                </TableBody>
              </Table>
            </TableContainer>
          </Paper>
        </Grid>
      )}
    </>
  );
}