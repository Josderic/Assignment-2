

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Employee Dashboard</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>

  <React.StrictMode>
    <App />
  </React.StrictMode>


    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={Dashboard />
        <Route path="/form" element={EmployeeForm />
      </Routes>
    </Router>
  

    <nav className="navbar navbar-expand-lg navbar-dark bg-dark px-3">
      <Link className="navbar-brand" to="/">Employee App</Link>
      <div className="collapse navbar-collapse">
        <ul className="navbar-nav ms-auto">
          <li className="nav-item">
            <Link className="nav-link" to="/">Home</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/form">Employee Form</Link>
          </li>
        </ul>
      </div>
    </nav>
    <div className="container mt-4">
      <h2>Employee Dashboard</h2>
      <table className="table table-bordered table-striped mt-3">
        <thead className="table-dark">
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
        
            <tr key={emp.id}>
              <td>{emp.id}</td>
              <td>{emp.name}</td>
              <td>{emp.email}</td>
            </tr>
         
        </tbody>
      </table>
    </div>
  

    <div className="container mt-4">
      <h2>Add Employee</h2>
      <form className="row g-3 mt-2" onSubmit={handleSubmit}>
        <div className="col-md-6">
          <label className="form-label">Name</label>
          <input type="text" name="name" className="form-control" onChange={handleChange} required />
        </div>
        <div className="col-md-6">
          <label className="form-label">Designation</label>
          <input type="text" name="designation" className="form-control" onChange={handleChange} required />
        </div>
        <div className="col-md-6">
          <label className="form-label">Location</label>
          <input type="text" name="location" className="form-control" onChange={handleChange} required />
        </div>
        <div className="col-md-6">
          <label className="form-label">Salary</label>
          <input type="number" name="salary" className="form-control" onChange={handleChange} required />
        </div>
        <div className="col-12">
          <button className="btn btn-primary" type="submit">Submit</button>
        </div>
      </form>
    </div>
  