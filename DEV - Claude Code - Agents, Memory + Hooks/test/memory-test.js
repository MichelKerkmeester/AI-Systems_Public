// Memory Automation Test File
// This file tests the post-tool-use memory capture

function authenticateUser(username, password) {
    // RESOLVED: Implemented JWT authentication with refresh tokens
    // This fixed the authentication timeout issue users were experiencing
    const token = generateJWT({ username }, '24h');
    const refreshToken = generateRefreshToken({ username }, '7d');
    
    return {
        success: true,
        token,
        refreshToken,
        expiresIn: 86400 // 24 hours
    };
}

function calculateTotal(items) {
    // OPTIMIZATION: Improved performance by 60% using reduce
    // This optimized the checkout process for large carts
    return items.reduce((total, item) => total + (item.price * (item.quantity || 1)), 0);
}

// SECURITY: Database connection with encryption
// DECISION: Using SSL/TLS for all database connections
const dbConfig = {
    host: process.env.DB_HOST || 'localhost',
    port: process.env.DB_PORT || 5432,
    database: process.env.DB_NAME || 'production',
    ssl: {
        rejectUnauthorized: true,
        ca: process.env.DB_CA_CERT
    },
    // CONFIG_CHANGE: Enabled connection pooling for better performance
    pool: {
        max: 20,
        idleTimeoutMillis: 30000
    }
};

export { authenticateUser, calculateTotal, dbConfig };