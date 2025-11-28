---
title: Admin Dashboard
draft: false
---

<style>
  .dashboard-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
  }
  .stat-card {
    background: rgba(255, 255, 255, 0.05);
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.1);
  }
  .stat-value {
    font-size: 2.5rem;
    font-weight: bold;
    color: var(--secondary);
  }
  .stat-label {
    font-size: 0.9rem;
    opacity: 0.8;
  }
  
  .heatmap-container {
    margin-top: 30px;
    overflow-x: auto;
  }
  .heatmap-grid {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 5px;
    min-width: 800px;
  }
  .heatmap-cell {
    aspect-ratio: 1;
    border-radius: 4px;
    position: relative;
    cursor: pointer;
    transition: transform 0.2s;
  }
  .heatmap-cell:hover {
    transform: scale(1.1);
    z-index: 10;
    border: 1px solid white;
  }
  .cell-tooltip {
    position: absolute;
    bottom: 100%;
    left: 50%;
    transform: translateX(-50%);
    background: #333;
    color: white;
    padding: 5px 10px;
    border-radius: 4px;
    font-size: 0.8rem;
    white-space: nowrap;
    display: none;
    pointer-events: none;
  }
  .heatmap-cell:hover .cell-tooltip {
    display: block;
  }
  
  .month-label {
    text-align: center;
    font-size: 0.8rem;
    margin-top: 5px;
    opacity: 0.7;
  }
</style>

# Dashboard

<div class="dashboard-grid">
  <div class="stat-card">
    <div class="stat-value" id="total-candidates">-</div>
    <div class="stat-label">Total Candidates</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" id="occupancy-rate">-</div>
    <div class="stat-label">Avg Occupancy (12m)</div>
  </div>
  <div class="stat-card">
    <div class="stat-value" id="peak-month">-</div>
    <div class="stat-label">Peak Month</div>
  </div>
</div>

## Occupancy Heatmap (Next 12 Months)

<div class="heatmap-container">
  <div class="heatmap-grid" id="heatmap">
    <!-- Populated by JS -->
  </div>
  <div class="heatmap-grid" id="heatmap-labels">
    <!-- Populated by JS -->
  </div>
</div>

<script>
  async function loadStats() {
    try {
      const response = await fetch('/api/stats');
      if (!response.ok) throw new Error('Failed to fetch stats');
      const data = await response.json();
      
      // Update Summary Cards
      document.getElementById('total-candidates').textContent = data.total_candidates;
      document.getElementById('occupancy-rate').textContent = data.avg_occupancy + '%';
      document.getElementById('peak-month').textContent = data.peak_month;
      
      // Render Heatmap
      const grid = document.getElementById('heatmap');
      const labels = document.getElementById('heatmap-labels');
      grid.innerHTML = '';
      labels.innerHTML = '';
      
      data.months.forEach(m => {
        // Cell
        const cell = document.createElement('div');
        cell.className = 'heatmap-cell';
        
        // Color based on occupancy percentage
        const occ = m.occupancy_percent;
        let color = 'rgba(255, 255, 255, 0.1)'; // Empty
        if (occ > 0) color = `rgba(76, 175, 80, ${0.2 + (occ/100 * 0.8)})`; // Green scale
        if (occ > 80) color = `rgba(255, 152, 0, ${0.2 + (occ/100 * 0.8)})`; // Orange high
        if (occ >= 100) color = 'rgba(244, 67, 54, 0.9)'; // Red full
        
        cell.style.backgroundColor = color;
        
        // Tooltip
        cell.innerHTML = `
          <div class="cell-tooltip">
            ${m.month}<br>
            ${m.count} / ${m.capacity} (${occ}%)
          </div>
        `;
        grid.appendChild(cell);
        
        // Label
        const label = document.createElement('div');
        label.className = 'month-label';
        // Format YYYY-MM to Short Month
        const date = new Date(m.month + '-01');
        label.textContent = date.toLocaleDateString('en-US', { month: 'short' });
        labels.appendChild(label);
      });
      
    } catch (e) {
      console.error(e);
      document.getElementById('total-candidates').textContent = 'Err';
    }
  }
  
  // Load on mount
  loadStats();
</script>
