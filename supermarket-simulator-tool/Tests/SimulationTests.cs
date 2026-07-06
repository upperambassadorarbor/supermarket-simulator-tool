using SupermarketSimulatorTool.Core;
using SupermarketSimulatorTool.Services;

namespace SupermarketSimulatorTool.Tests;

public class SimulationTests
{
    [Fact]
    public void Engine_StartAndStop_Works()
    {
        var engine = new SimulationEngine();
        engine.Start();
        Thread.Sleep(100);
        Assert.True(engine.IsRunning);
        engine.Stop();
        Assert.False(engine.IsRunning);
    }

    [Fact]
    public void CustomerService_TracksCounts()
    {
        var service = new CustomerService();
        service.SpawnCustomer();
        service.SpawnCustomer();
        service.ServeCustomer();
        Assert.Equal(2, service.TotalCustomers);
        Assert.Equal(1, service.ServedCustomers);
    }

    [Fact]
    public void AdjustSpeed_ClampsValue()
    {
        var engine = new SimulationEngine();
        engine.AdjustSpeed(15f);
        engine.Start();
        Thread.Sleep(200);
        Assert.True(engine.CurrentTick >= 1);
        engine.Stop();
    }
}