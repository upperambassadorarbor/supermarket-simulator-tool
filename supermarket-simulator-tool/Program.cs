using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using SupermarketSimulatorTool.Core;
using SupermarketSimulatorTool.Services;

var host = Host.CreateDefaultBuilder(args)
    .ConfigureServices((context, services) =>
    {
        services.AddSingleton<ICustomerService, CustomerService>();
        services.AddSingleton<ISimulationEngine, SimulationEngine>();
        services.AddHostedService<SimulationHost>();
    })
    .Build();

await host.RunAsync();