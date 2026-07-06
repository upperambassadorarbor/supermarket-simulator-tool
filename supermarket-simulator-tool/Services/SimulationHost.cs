using Microsoft.Extensions.Hosting;
using SupermarketSimulatorTool.Core;
using SupermarketSimulatorTool.Services;

namespace SupermarketSimulatorTool.Services;

public class SimulationHost : BackgroundService
{
    private readonly ISimulationEngine _engine;
    private readonly ICustomerService _customerService;

    public SimulationHost(ISimulationEngine engine, ICustomerService customerService)
    {
        _engine = engine;
        _customerService = customerService;
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        _engine.Start();

        while (!stoppingToken.IsCancellationRequested)
        {
            _customerService.SpawnCustomer();
            if (_customerService.TotalCustomers > _customerService.ServedCustomers)
                _customerService.ServeCustomer();

            Console.WriteLine($"Tick {_engine.CurrentTick}: Customers={_customerService.TotalCustomers}, Served={_customerService.ServedCustomers}");
            await Task.Delay(500, stoppingToken);
        }

        _engine.Stop();
    }
}