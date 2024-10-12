    const ctx = document.getElementById('ipoChart').getContext('2d');
    const ipoChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            // labels: ['Upcoming', 'New Listed', 'Ongoing'],
            datasets: [{
                label: 'IPO Data',
                data: [15, 40, 25],
                // data: [ipo_upcoming, ipo_new_listed, ipo_ongoing]
                backgroundColor: ['#5A6EF5', '#9399FC', '#C5C6FC'],
                borderWidth: 0,
                hoverBackgroundColor: [
                    // 'gray'
                    'rgba(128, 128, 128, 0.5)'
                ],
            }]
        },
        options: {
            responsive: true,
            cutout: '70%',
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            return tooltipItem.label + ': ' + tooltipItem.raw;
                        }
                    }
                }
            }
        }
    });
